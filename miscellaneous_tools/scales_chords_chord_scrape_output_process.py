CHORD_DEGREE_NAME_INDEXES = {
    'm2': 1,
    '2': 2,
    'm3': 3,
    '3': 4,
    '4': 5,
    'm5': 6,
    '5': 7,
    'â™¯5': 8,
    'm6': 8,
    '6': 9,
    'm7': 10,
    '7': 11,
    '8': 12,
    'm9': 13,
    '9': 14,
    'm10': 15,
    '10': 16,
    '11': 17,
    'm12': 18,
    '12': 19,
    'm13': 20,
    '13': 21,
}


with open('scales_chords_chord_scrape_output_modified.txt', 'r') as f:
    with open('scales_chords_chord_scrape_code_output.txt', 'w') as o:
        for line in f.readlines()[1:]:
            chord_data = line.split('|')
            if chord_data[0] == '':
                continue
            class_name = chord_data[0] + 'ChordContext'
            primary_symbol = '_' + chord_data[1][1:]
            name = chord_data[2]
            chord_degree_names = chord_data[3].split(', ')
            chord_degrees = [CHORD_DEGREE_NAME_INDEXES[i] for i in chord_degree_names if i != 'R']
            alternative_names = chord_data[4].strip('\n')
            code_text_start = f"{class_name} = WesternTrueOctavedChordContext(chord_degrees={chord_degrees}, " + \
                              f"name='{name}', primary_symbol='{primary_symbol}'"
            if alternative_names:
                code_text = code_text_start + \
                    f", alternative_names={['_' + i[1:] for i in alternative_names.split(', ')]})"
            else:
                code_text = code_text_start + ')'
            o.write(code_text + '\n')
