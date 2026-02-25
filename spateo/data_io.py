from anndata import AnnData, concat, read_h5ad

try:
    # anndata < 0.12
    from anndata import read
except ImportError:
    # anndata >= 0.12 removed `read`
    read = read_h5ad

try:
    # anndata < 0.12 export these at top-level
    from anndata import (
        read_csv,
        read_excel,
        read_hdf,
        read_loom,
        read_mtx,
        read_text,
        read_umi_tools,
        read_zarr,
    )
except ImportError:
    from anndata.io import (
        read_csv,
        read_excel,
        read_hdf,
        read_loom,
        read_mtx,
        read_text,
        read_umi_tools,
        read_zarr,
    )
