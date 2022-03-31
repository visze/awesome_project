import click
import matplotlib.pyplot as plt


# options
@click.command()
@click.option('--condition',
              'condition',
              required=True,
              type=click.Choice(['untreated', 'treated'], case_sensitive=False),
              help='Input condition')
@click.option('--output',
              'output_file',
              required=True,
              type=click.Path(writable=True),
              help='Output PNG file')
def cli(condition, output_file):

    switcher = {
        "untreated": "green",
        "treated": "red",
    }

    fig, ax = plt.subplots(nrows=1, ncols=1)

    ax.set_facecolor(switcher.get(condition, "blue"))
    plt.savefig(output_file)


if __name__ == '__main__':
    cli()
