from jinja2 import Environment, FileSystemLoader
import os

class ReportGenerator:
    def __init__(self, src_only, dest_only, both):
        self.src_only = src_only
        self.dest_only = dest_only
        self.both = both

    def generate_html_report(self, output_file):
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
        template = env.get_template('report_template.html')
        html_content = template.render(
            src_only=self.src_only.to_html(index=False),
            dest_only=self.dest_only.to_html(index=False),
            both=self.both.to_html(index=False)
        )

        with open(output_file, 'w') as file:
            file.write(html_content)
