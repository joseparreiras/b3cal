import os

def update():
    """
    Update holidays database from ANBIMA website. If successful, saves the database to `tools/holidays.csv`.

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # ANBIMA url
        url = "https://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls"
        holidays = pd.read_excel(url)
        holidays.dropna(inplace=True)  # Drop latest rows with footnotes
        holidays = holidays["Data"]
        # Export to `tools` folder
        os.makedirs("tools", exist_ok=True)
        holidays.to_csv("tools/holidays.csv", index=False)
        return True
    except:
        print("Failed to Update Holidays")
        return False
