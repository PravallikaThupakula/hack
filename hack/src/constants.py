entity_unit_map = {
    'width': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'depth': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'height': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'item_weight': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'maximum_weight_recommendation': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'voltage': {'kilovolt', 'millivolt', 'volt'},
    'wattage': {'kilowatt', 'watt'},
    'item_volume': {'centilitre',
        'cubic foot',
        'cubic inch',
        'cup',
        'decilitre',
        'fluid ounce',
        'gallon',
        'imperial gallon',
        'litre',
        'microlitre',
        'millilitre',
        'pint',
        'quart'}
}

unit_full_name_map = {
    'cm': 'centimetre',
    'ft': 'foot',
    'in': 'inch',
    'm': 'metre',
    'mm': 'millimetre',
    'yd': 'yard',
    'g': 'gram',
    'kg': 'kilogram',
    'µg': 'microgram',
    'mg': 'milligram',
    'oz': 'ounce',
    'lb': 'pound',
    'ton': 'ton',
    'kv': 'kilovolt',
    'mv': 'millivolt',
    'v': 'volt',
    'kw': 'kilowatt',
    'w': 'watt',
    'cl': 'centilitre',
    'cu ft': 'cubic foot',
    'cu in': 'cubic inch',
    'cup': 'cup',
    'dl': 'decilitre',
    'fl oz': 'fluid ounce',
    'gal': 'gallon',
    'imp gal': 'imperial gallon',
    'l': 'litre',
    'µl': 'microlitre',
    'ml': 'millilitre',
    'pt': 'pint',
    'qt': 'quart'
}

allowed_units = {unit for entity in entity_unit_map for unit in entity_unit_map[entity]}