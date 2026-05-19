import re
import sys

def fix_mockform(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Fix 1: key in map
    content = re.sub(r'key=\{index\}', r'key={header.id}', content)

    # Fix 2: add type="button" to the remove button
    # We'll find the button that has onClick={() => removeHeader(index)} and add type="button"
    # We'll do a replacement that captures the button opening and adds the type attribute.
    # The pattern: <button\n\t\t\t\t\t\t\t\tonClick={() => removeHeader(index)}
    # We'll replace with: <button type="button"\n\t\t\t\t\t\t\t\tonClick={() => removeHeader(index)}
    content = re.sub(
        r'(<button\n\t\t\t\t\t\t\t\tonClick=\{\) => removeHeader\(index\)\})',
        r'<button type="button"\n\t\t\t\t\t\t\t\tonClick={() => removeHeader(index)}>',
        content,
        flags=re.MULTILINE
    )

    # Fix 3: Associate labels with inputs by adding htmlFor and id
    # We'll do for each known label by replacing the label and the following element.
    # We'll do a series of replacements for each field.

    # HTTP Method: label and select
    # We'll change the label to have htmlFor="method-select" and add id="method-select" to the select.
    # We'll do two steps: first, change the label.
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">HTTP Method</label>)',
        r'<label htmlFor="method-select" className="block text-sm font-medium mb-1">HTTP Method</label>',
        content
    )
    # Then, add id to the select. We'll find the select that follows the label (after some whitespace and possibly the div).
    # Since the structure is regular, we can target the select that has value={formData.method}
    content = re.sub(
        r'(<select\n\t\t\t\t\t\t\tvalue={formData\.method})',
        r'\1 id="method-select"',
        content
    )

    # Path: label and input
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">Path</label>)',
        r'<label htmlFor="path-input" className="block text-sm font-medium mb-1">Path</label>',
        content
    )
    content = re.sub(
        r'(<input\n\t\t\t\t\t\t\ttype="text"\n\t\t\t\t\t\t\tvalue={formData\.path})',
        r'\1 id="path-input"',
        content
    )

    # Status Code: label and select
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">Status Code</label>)',
        r'<label htmlFor="status-code-select" className="block text-sm font-medium mb-1">Status Code</label>',
        content
    )
    content = re.sub(
        r'(<select\n\t\t\t\t\t\t\tvalue={formData\.statusCode})',
        r'\1 id="status-code-select"',
        content
    )

    # Description: label and input
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">Description</label>)',
        r'<label htmlFor="description-input" className="block text-sm font-medium mb-1">Description</label>',
        content
    )
    content = re.sub(
        r'(<input\n\t\t\t\t\t\t\ttype="text"\n\t\t\t\t\t\t\tvalue={formData\.description})',
        r'\1 id="description-input"',
        content
    )

    # Response Body: label and textarea
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">\n\t\t\t\t\t\tResponse Body\n\t\t\t\t\t</label>)',
        r'<label htmlFor="response-body-textarea" className="block text-sm font-medium mb-1">\n\t\t\t\t\t\tResponse Body\n\t\t\t\t\t</label>',
        content,
        flags=re.MULTILINE
    )
    content = re.sub(
        r'(<textarea\n\t\t\t\t\t\t\tvalue={formData\.responseBody})',
        r'\1 id="response-body-textarea"',
        content
    )

    # Response Headers: label and div (the div that contains the map)
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">\n\t\t\t\t\t\tResponse Headers\n\t\t\t\t\t</label>)',
        r'<label htmlFor="response-headers-div" className="block text-sm font-medium mb-1">\n\t\t\t\t\t\tResponse Headers\n\t\t\t\t\t</label>',
        content,
        flags=re.MULTILINE
    )
    # Find the div that has className="space-y-2" and is directly after the label (with some whitespace and the div opening)
    # We'll add id="response-headers-div" to that div.
    content = re.sub(
        r'(<div className="space-y-2">)',
        r'<div id="response-headers-div" className="space-y-2">',
        content
    )

    # Active: label and checkbox input
    content = re.sub(
        r'(<label className="text-sm font-medium text-gray-700">Active</label>)',
        r'<label htmlFor="active-checkbox" className="text-sm font-medium text-gray-700">Active</label>',
        content
    )
    content = re.sub(
        r'(<input\n\t\t\t\t\t\t\ttype="checkbox"\n\t\t\t\t\t\t\tchecked={formData\.active})',
        r'\1 id="active-checkbox"',
        content
    )

    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fix_mockform.py <filepath>")
        sys.exit(1)
    fix_mockform(sys.argv[1])