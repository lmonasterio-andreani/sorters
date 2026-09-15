#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sincronizador Automático de Aplicaciones SPP desde GitOps Platform
===================================================================
Fuente oficial: https://ui-gitops-prod.apps.andreani.com.ar/aplicaciones?projectId=51
Backend API: https://github-wizard-api-gitops-prod.apps.andreani.com.ar/api/v1/

Modos de Operación:
1. Vía API REST directa (pasando token Bearer con variable GITOPS_TOKEN o argumento --token).
2. Vía Archivo Excel exportado (detecta automáticamente el archivo más reciente en relevamiento/planillas/).
"""

import os
import sys
import glob
import json
import shutil
import ssl
import argparse
import urllib.request
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ID = 51
GITOPS_API_URL = f"https://github-wizard-api-gitops-prod.apps.andreani.com.ar/api/v1/applications?projectId={PROJECT_ID}"
OUTPUT_MD_PATH = os.path.join("docs", "06-ecosistema-spp.md")
OUTPUT_JSON_PATH = os.path.join("docs", "assets", "spp-apps.json")
PLANILLAS_DIR = os.path.join("relevamiento", "planillas")

CATEGORIES = {
    "1. Integración con Sorters (Clasificación Automatizada)": [
        "job-spptovertical",
        "sortervertical-api",
        "spptovertical-suscriber",
        "vertical-sorter-worker",
        "verticaltospp-publisher",
        "integration-sorters-api"
    ],
    "2. Ingesta, Altas y Procesamiento Core": [
        "spp-altas-api",
        "spp-altas-suscriber",
        "procesamiento-api",
        "publisher-events-spp",
        "bulto-informado-worker",
        "oneclick-api"
    ],
    "3. Consolidación de Bultos y Contenedores": [
        "consolidacion-api",
        "consolidacionautomatica-api",
        "consolidacion-bultos-worker",
        "contenedores-suscriber",
        "contenedores-to-integra",
        "cierredecontendorspp-worker",
        "cierredecontenedorspp-worker"
    ],
    "4. Medición, Aforo y Geocercas": [
        "eventosdeaforo-api",
        "geocerca-consumer"
    ],
    "5. Distribución y Abastecimiento a Sucursales": [
        "spp-sucursal-abastecedora-worker",
        "sucursal-abastecedora-spp-worker"
    ],
    "6. Interfaces de Usuario y Aplicaciones Web (React)": [
        "spp-ui",
        "spp-dashboard-ui",
        "trackinginternoui"
    ],
    "7. Trazabilidad Interna, Reportes y Archivos": [
        "tracking-api",
        "reportes-api",
        "generador-de-archivo-worker"
    ],
    "8. Gateways, Puentes e Integraciones de Negocio": [
        "gateway-hop-api",
        "mq-bridge-api",
        "natura-spp-publisher"
    ]
}


def fetch_from_api(token):
    """Intenta descargar las aplicaciones directamente desde la API de GitOps."""
    print(f"[*] Conectando a GitOps API: {GITOPS_API_URL} ...")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    req = urllib.request.Request(GITOPS_API_URL, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            if response.getcode() == 200:
                data = json.loads(response.read().decode('utf-8'))
                print(f"[+] Conexión exitosa. Se recibieron datos de la API de GitOps.")
                return data
    except Exception as e:
        print(f"[-] No se pudo sincronizar vía API: {e}")
    return None


def fetch_from_excel():
    """Busca el archivo Excel de exportación más reciente en relevamiento/planillas/."""
    pattern = os.path.join(PLANILLAS_DIR, "aplicaciones*.xlsx")
    files = glob.glob(pattern)
    if not files:
        # Intenta con cualquier archivo xlsx en planillas
        files = glob.glob(os.path.join(PLANILLAS_DIR, "*.xlsx"))
        files = [f for f in files if "aplicaciones" in os.path.basename(f).lower()]

    if not files:
        print(f"[-] No se encontraron archivos de exportación en {PLANILLAS_DIR}")
        return None

    # Ordenar por fecha de modificación más reciente
    files.sort(key=os.path.getmtime, reverse=True)
    latest_file = files[0]
    print(f"[*] Procesando archivo local más reciente: {latest_file}")

    # Copia temporal segura para evitar bloqueos si el archivo está abierto en Excel
    temp_path = "temp_sync_app.xlsx"
    try:
        shutil.copyfile(latest_file, temp_path)
    except PermissionError:
        os.system(f'powershell -Command "Copy-Item -Path \'{latest_file}\' -Destination \'{temp_path}\' -Force"')

    try:
        wb = openpyxl.load_workbook(temp_path)
        sheet = wb.active
        headers = [str(c.value).strip() if c.value is not None else f"Col{i}" for i, c in enumerate(sheet[1])]
        
        apps = []
        for r in range(2, sheet.max_row + 1):
            vals = [str(c.value).strip() if c.value is not None else "" for c in sheet[r]]
            if any(vals):
                item = dict(zip(headers, vals))
                apps.append(item)
        print(f"[+] Se leyeron {len(apps)} aplicaciones desde el archivo Excel.")
        return apps
    finally:
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass


def generate_markdown(apps):
    """Genera el documento Markdown estructurado con diseño Cartesian."""
    apps.sort(key=lambda x: x.get('Nombre App', '').lower())

    all_assigned = set()
    for sublist in CATEGORIES.values():
        all_assigned.update(sublist)

    unassigned = [a.get('Nombre App') for a in apps if a.get('Nombre App') not in all_assigned]
    active_categories = dict(CATEGORIES)
    if unassigned:
        active_categories["9. Otras Aplicaciones y Servicios"] = unassigned

    doc_lines = []
    doc_lines.append("# 06. Ecosistema SPP (Sistema de Paquetería y Procesamiento)\n")
    doc_lines.append("El **SPP (`tyd-spp`)** es la plataforma troncal de Andreani responsable de orquestar la paquetería, las altas de envíos, los aforos dinámicos, la consolidación en contenedores y la interfaz bidireccional con los clasificadores automáticos (**Sorters**).\n")
    doc_lines.append("> 📁 **Fuente Oficial:** Sincronizado automáticamente desde la plataforma de arquitectura [**GitOps Andreani**](https://ui-gitops-prod.apps.andreani.com.ar/aplicaciones?view=table&section=detalles&projectId=51) | Proyecto: `tyd-spp` (ID: 51) | Owner Técnico: `sbecerra@andreani.com`.\n")
    doc_lines.append("---\n")
    doc_lines.append("## 🗺️ Arquitectura de Integración: ¿Cómo interactúan SPP y los Sorters?\n")
    doc_lines.append("Los Sorters físicos (Vertical, Wayzim, etc.) no toman decisiones de ruteo de forma aislada. Dependen de SPP para saber hacia qué rampa expulsar cada bulto y para notificar la confirmación del pesaje y la clasificación:\n")
    doc_lines.append("```mermaid\ngraph TD\n    subgraph Ingesta y Preparación en SPP\n        K1[\"Kafka: OrdenEnvioCreada\"] --> AS[\"spp-altas-suscriber\"]\n        AS --> AA[\"spp-altas-api\"]\n        AA --> DB[(\"DBSORTER (SQL Server)\")]\n    end\n\n    subgraph Despacho hacia Sorter\n        DB --> SVS[\"spptovertical-suscriber\"]\n        SVS --> IV[(\"Integración Vertical\")]\n        IV --> HW[\"Software Proveedor / PLC Sorter\"]\n    end\n\n    subgraph Ciclo de Clasificación y Retorno\n        HW -- \"Clasificado Exitoso\" --> VTP[\"verticaltospp-publisher\"]\n        VTP --> SVA[\"sortervertical-api\"]\n        SVA --> EAF[\"eventosdeaforo-api\"]\n        EAF --> PES[\"publisher-events-spp\"]\n        PES --> K2[\"Kafka: Eventos SPP / Trazabilidad\"]\n    end\n\n    subgraph Loop de Resiliencia (Rampa 6)\n        HW -- \"Rechazo / Sin Destino\" --> R6[\"Expulsión a Rampa 6\"]\n        R6 --> JOB[\"job-spptovertical\"]\n        JOB -- \"Reinyecta para re-clasificación\" --> IV\n    end\n```\n")
    doc_lines.append("---\n")
    doc_lines.append("## 📊 Resumen Ejecutivo del Parque de Aplicaciones\n")

    total_apps = len(apps)
    activas = sum(1 for a in apps if a.get('Estado') == 'Activa')
    desarrollo = sum(1 for a in apps if a.get('Estado') == 'En Desarrollo')
    desactivadas = sum(1 for a in apps if a.get('Estado') == 'Desactivada')
    dotnet = sum(1 for a in apps if a.get('Framework') == 'NET')
    react = sum(1 for a in apps if a.get('Framework') == 'REACT')

    doc_lines.append(f"| Métrica | Valor | Observaciones |")
    doc_lines.append(f"| :--- | :---: | :--- |")
    doc_lines.append(f"| **Total de Aplicaciones Registradas** | **{total_apps}** | Catálogo oficial en `operations-innovation` |")
    doc_lines.append(f"| **Aplicaciones Activas en Producción** | **{activas}** | Servicios productivos operando en planta |")
    doc_lines.append(f"| **En Desarrollo / Modernización** | **{desarrollo}** | Módulos en construcción o evolución |")
    doc_lines.append(f"| **Desactivadas / Legadas** | **{desactivadas}** | Servicios retirados |")
    doc_lines.append(f"| **Stack Tecnológico Principal** | **.NET ({dotnet}) / React ({react})** | C# (APIs/Workers) y JavaScript/TypeScript (Frontends) |")
    doc_lines.append("\n---\n")

    app_dict = {a.get('Nombre App'): a for a in apps}

    for cat_title, app_names in active_categories.items():
        doc_lines.append(f"## {cat_title}\n")
        doc_lines.append("| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |")
        doc_lines.append("| :--- | :--- | :---: | :---: | :---: | :--- |")
        for name in app_names:
            a = app_dict.get(name)
            if not a:
                continue
            template = a.get('Template', '')
            framework = a.get('Framework', '')
            tipo = f"{framework} ({template})" if template else framework
            estado = a.get('Estado', '')
            qg = a.get('Quality Gate', '')
            cov = a.get('Coverage', '')
            repo = a.get('Repositorio', '')
            repo_link = f"[`{name}`]({repo})" if repo else f"`{name}`"
            
            estado_badge = f"🟢 {estado}" if estado == "Activa" else (f"🟡 {estado}" if estado == "En Desarrollo" else f"⚪ {estado}")
            qg_badge = "✅ OK" if qg == "OK" else ("❌ ERROR" if qg == "ERROR" else "⚪ Sin datos")
            cov_str = f"{cov}%" if cov and cov != "Sin datos" else "-"
            
            doc_lines.append(f"| **{repo_link}** | {tipo} | {estado_badge} | {cov_str} | {qg_badge} | [Ver Repositorio ↗]({repo}) |")
        doc_lines.append("\n---\n")

    content = "\n".join(doc_lines)
    os.makedirs(os.path.dirname(OUTPUT_MD_PATH), exist_ok=True)
    with open(OUTPUT_MD_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[+] Archivo generado exitosamente: {OUTPUT_MD_PATH}")

    # Guardar también el dump JSON en docs/assets/spp-apps.json para consumo estructurado
    os.makedirs(os.path.dirname(OUTPUT_JSON_PATH), exist_ok=True)
    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(apps, f, indent=2, ensure_ascii=False)
    print(f"[+] Archivo JSON generado: {OUTPUT_JSON_PATH}")


def main():
    parser = argparse.ArgumentParser(description="Sincronizador GitOps SPP")
    parser.add_argument("--token", help="Bearer Token para la API de GitOps", default=os.getenv("GITOPS_TOKEN"))
    args = parser.parse_args()

    apps = None
    if args.token:
        apps = fetch_from_api(args.token)

    if not apps:
        apps = fetch_from_excel()

    if not apps:
        print("[-] Error: No se pudo obtener la información de las aplicaciones.")
        sys.exit(1)

    generate_markdown(apps)
    print("\n========================================================")
    print(" ¡Sincronización completada con éxito!")
    print("========================================================")


if __name__ == "__main__":
    main()
