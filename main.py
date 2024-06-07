import Config
import DatabaseConnection
import Mapping
import DataExtractor
import DataComparer
import ReportGenerator

def main(config_file, mappings_file, output_file):
    config = Config(config_file)
    src_conn = DatabaseConnection(config.source_db)
    dest_conn = DatabaseConnection(config.destination_db)

    mappings = Mapping(mappings_file)

    src_extractor = DataExtractor(src_conn, mappings.src_table, mappings.src_columns)
    dest_extractor = DataExtractor(dest_conn, mappings.dest_table, mappings.dest_columns)

    src_df = src_extractor.extract()
    dest_df = dest_extractor.extract()

    comparer = DataComparer()
    src_only, dest_only, both = comparer.compare(src_df, dest_df, mappings.key_columns)

    report_generator = ReportGenerator(src_only, dest_only, both)
    report_generator.generate_html_report(output_file)

if __name__ == "__main__":
    main('db_config.json', 'mappings.json', 'report.html')
