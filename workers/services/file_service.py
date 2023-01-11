def save_file(df, path):
    df.to_excel(path, index=False)
