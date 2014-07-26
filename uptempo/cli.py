import click
import jinja2
import json

def update_file(file_name, dict):
    # read text file as a template
    try:
        f = open(file_name, 'r')
        t = jinja2.Template(f.read())
        f.close()
    except:
        click.echo('Skipping file %s' % file_name)
        return
    
    # write file with value replacements
    click.echo('Updating file %s' % file_name)
    f = open(file_name, 'w')
    f.write(t.render(dict))
    f.write('\n')
    f.close()

@click.command()
@click.argument('json_file', type=click.File('r'))
@click.argument('text_file', nargs=-1)
def cli(json_file, text_file):
    """Update templated text files with values contained in a JSON data file."""
    
    # read json data
    click.echo('Reading JSON file for values')
    d = json.loads(json_file.read())
    
    # check for files to update
    if len(text_file) == 0:
        click.echo('No files to update, exiting')
        return
    
    # update all parsed files
    for fn in text_file:
        update_file(fn, d)

if __name__ == '__main__':
    cli()
