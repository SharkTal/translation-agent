import os

import translation_agent as ta


if __name__ == "__main__":
    source_lang, target_lang, country = "Chinese", "English", "US"

    relative_path = "/workspaces/translation-agent/examples/sample-texts/hwphone-c2.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))

    full_path = os.path.join(script_dir, relative_path)

    with open(full_path, encoding="utf-8") as file:
        source_text = file.read()

    print(f"Source text:\n\n{source_text}\n------------\n")

    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )

    print(f"Translation:\n\n{translation}")

        # Define the output file path
    output_file_name = "translated_hwphone-c2.txt"
    output_file_path = os.path.join(script_dir, output_file_name)

    # Save the translation to the output file
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(translation)

    print(f"\nTranslation saved to {output_file_path}")
