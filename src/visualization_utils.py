import matplotlib.pyplot as plt
import seaborn as sns

def bar_plot(df, x, y, title, save_path=None):
    plt.figure(figsize=(8, 5))
    sns.barplot(x=x, y=y, data=df)
    plt.title(title)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()


def line_plot(df, x, y, title, save_path=None):
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=x, y=y, data=df, marker="o")
    plt.title(title)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()


# -------- TEST BLOCK --------
if __name__ == "__main__":
    print("Testing visualization_utils module...")
