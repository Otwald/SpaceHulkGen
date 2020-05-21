import click
from basic_gen import Basic


@click.command()
@click.option(
    '--size', '-s', default=4, help='How Many Group Members?'
)
@click.option(
    '--level', '-l', default="n", help='SkillLevel of the Group, n=Notive s=Skilled v=Veteran'
)
@click.option(
    '--optional', '-o', default="True", help='Optional Generations rules True or False'
)
def main(size, level, optional):
    main = Basic(size, level, optional)
    main.mainLoop()


if __name__ == '__main__':
    main()
