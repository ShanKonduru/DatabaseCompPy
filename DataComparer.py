class DataComparer:
    @staticmethod
    def compare(src_df, dest_df, key_columns):
        src_only = src_df.merge(dest_df, how='left', indicator=True, on=key_columns).query('_merge == "left_only"').drop('_merge', axis=1)
        dest_only = dest_df.merge(src_df, how='left', indicator=True, on=key_columns).query('_merge == "left_only"').drop('_merge', axis=1)
        both = src_df.merge(dest_df, how='inner', on=key_columns)
        return src_only, dest_only, both
