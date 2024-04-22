# Definition der Klasse für die Verarbeitung der Mitgliederdaten
import ast


class Mitgliederdatenverarbeitung:
    @staticmethod
    def process_member_data(file_path):
        members = []
        try:
            with open(file_path, 'r') as file:
                # Lese den Inhalt der Datei
                content = file.read()
                # Entferne das Präfix "members = " aus dem Inhalt
                content = content.replace("members =", "")
                # Verwende ast.literal_eval, um den Inhalt als Python-Code zu interpretieren
                parsed_content = ast.literal_eval(content.strip())
                if isinstance(parsed_content, list):
                    members = parsed_content
                else:
                    print("Die Datei enthält keine Liste von Mitgliedern.")
        except Exception as e:
            print(f"Fehler beim Verarbeiten der Datei: {e}")
        return members