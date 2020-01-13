import matplotlib.pyplot as plt

def rectangle_grid(nplots, ncols):
    height_coefs = {
        2: 5.5,
        3: 4.5,
        4: 3.7,
        5: 3
    }
    height_coef = height_coefs[ncols]
    full_nrows, cols_in_last_row = divmod(nplots, ncols)
    nrows = full_nrows + bool(cols_in_last_row)
    fig, ax = plt.subplots(nrows = nrows, ncols=ncols, figsize=(16, height_coef*nrows))
    if cols_in_last_row != 0:
        for col in range(cols_in_last_row, ncols):
            if nrows != 1:
                ax[-1][col].axis('off')
            else:
                ax[col].axis('off')
    return fig, ax.reshape(-1)