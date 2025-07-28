import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    while True:
        start = html.find('<')
        end = html.find('>', start)
        if start == -1 or end == -1:
            break
        html = html[:start] + html[end+1:]

    with open(result_file, 'w', encoding='utf-8') as out_file:
        out_file.write(html)

