with open('scales_chords_chord_scrape_output_modified.txt', 'r') as f:
    with open('scales_chords_chord_scrape_code_output.txt', 'w') as o:
        for line in f.readlines()[1:]:
            scale_data = line.split('|')
            class_name = scale_data[0] + 'ScaleContext'
            primary_name = scale_data[1]
            scale_degrees = list(map(int, scale_data[2].split(', ')))
            alternative_names = scale_data[4].strip('\n')
            code_text_start = f"{class_name} = WesternTrueOctavedScaleContext(scale_degrees={scale_degrees}, " + \
                              f"primary_name='{primary_name}'"
            if alternative_names:
                code_text = code_text_start + f", alternative_names={alternative_names.split(', ')})"
            else:
                code_text = code_text_start + ')'
            o.write(code_text + '\n')
