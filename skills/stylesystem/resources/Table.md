# Table Components

**Imports:**
```tsx
import {
  TableContainer,
  Tablehead,
  TableRow,
  TableFooter,
  TablePagination
} from "@architecture-it/stylesystem";
// MUI primitives used alongside:
import { Table, TableBody, TableCell } from "@mui/material";
```

The stylesystem provides styled wrappers for MUI table components. You assemble the full table by combining stylesystem components with standard MUI primitives.

## TableContainer

The outer wrapper, renders as `Paper` + MUI `TableContainer`.

| Prop | Type | Description |
|------|------|-------------|
| `children` | `ReactNode` | Full table markup |
| `classes` | `{ root?, paper? }` | CSS slot overrides |

## Tablehead Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `headers` | `HeaderItem[]` | ✅ | Column definition array |

### `HeaderItem` shape

```ts
interface HeaderItem {
  label: string;           // Column header text
  sortable?: boolean;      // Shows sort icon if true
  align?: "left" \| "center" \| "right";
  width?: string \| number;
}
```

## TableRow Props

Styled `<tr>` row wrapper:

| Prop | Type | Description |
|------|------|-------------|
| `onClick` | `() => void` | Makes the row clickable (pointer cursor) |
| `selected` | `boolean` | Highlights row as selected |
| `classes` | `{ root? }` | CSS slot overrides |
| `children` | `ReactNode` | `<TableCell>` elements |

## TableFooter Props

| Prop | Type | Description |
|------|------|-------------|
| `children` | `ReactNode` | Footer row content |

## TablePagination Props

Extends MUI `TablePaginationProps`:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `count` | `number` | ✅ | Total rows |
| `page` | `number` | ✅ | Current page (0-indexed) |
| `rowsPerPage` | `number` | ✅ | Rows per page |
| `onPageChange` | `(event, page) => void` | ✅ | Page change handler |
| `rowsPerPageOptions` | `number[]` | `[10, 25, 50]` | Options for rows per page dropdown |
| `onRowsPerPageChange` | `(event) => void` | | Handler |
| `labelRowsPerPage` | `string` | | Label for the rows-per-page selector |

## Full Usage Example

```tsx
import {
  TableContainer, Tablehead, TableRow, TableFooter, TablePagination
} from "@architecture-it/stylesystem";
import { Table, TableBody, TableCell } from "@mui/material";

const headers = [
  { label: "ID", sortable: false },
  { label: "Nombre", sortable: true },
  { label: "Estado", sortable: true },
  { label: "Fecha", sortable: false, align: "right" as const },
];

function DataTable({ rows }: { rows: Row[] }) {
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

  const paginated = rows.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage);

  return (
    <TableContainer>
      <Table>
        <Tablehead headers={headers} />
        <TableBody>
          {paginated.map((row) => (
            <TableRow key={row.id} onClick={() => handleRowClick(row.id)}>
              <TableCell>{row.id}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.status}</TableCell>
              <TableCell align="right">{row.date}</TableCell>
            </TableRow>
          ))}
        </TableBody>
        <TableFooter>
          <TablePagination
            count={rows.length}
            page={page}
            rowsPerPage={rowsPerPage}
            onPageChange={(_, p) => setPage(p)}
            onRowsPerPageChange={(e) => {
              setRowsPerPage(parseInt(e.target.value, 10));
              setPage(0);
            }}
          />
        </TableFooter>
      </Table>
    </TableContainer>
  );
}
```

## Empty state

```tsx
<TableBody>
  {rows.length === 0 ? (
    <TableRow>
      <TableCell colSpan={headers.length} align="center">
        <Typography color="secondary">No hay resultados.</Typography>
      </TableCell>
    </TableRow>
  ) : (
    rows.map((row) => (
      <TableRow key={row.id}>
        {/* cells */}
      </TableRow>
    ))
  )}
</TableBody>
```

## With loading skeleton

```tsx
import { TableRowSkeleton } from "@architecture-it/stylesystem";

<TableBody>
  {loading
    ? Array.from({ length: rowsPerPage }).map((_, i) => (
        <TableRowSkeleton key={i} columns={headers.length} />
      ))
    : rows.map((row) => (
        <TableRow key={row.id}>{/* cells */}</TableRow>
      ))
  }
</TableBody>
```

## Notes

- `TableCell` is imported directly from MUI — stylesystem does not export a custom one.
- `TableBody` is also from MUI; `TableContainer`, `Tablehead`, `TableRow`, `TableFooter`, `TablePagination` are from stylesystem.
- `TablePagination` is placed inside `TableFooter` inside the `<Table>` — do NOT place it outside the `<Table>`.
- Use `TableContainer` (not `Paper`) as the outer wrapper — it handles the correct shadow and border-radius.
