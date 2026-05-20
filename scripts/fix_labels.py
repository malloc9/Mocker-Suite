import re
import sys

def fix_labels(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # We'll process line by line and make changes.
    # We'll look for the label and then the next input/select/textarea or div.

    # However, the structure is not always one line after. We'll use a simple approach:
    # We'll do a series of replacements on the entire string.

    content = ''.join(lines)

    # Fix for HTTP Method
    # Label: <label className="block text-sm font-medium mb-1">HTTP Method</label>
    # Select: <select ... value={formData.method}
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">HTTP Method</label>)',
        r'<label htmlFor="method-select" className="block text-sm font-medium mb-1">HTTP Method</label>',
        content
    )
    content = re.sub(
        r'(<select\n\s*value={formData\.method})',
        r'\1 id="method-select"',
        content
    )

    # Fix for Path
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">Path</label>)',
        r'<label htmlFor="path-input" className="block text-sm font-medium mb-1">Path</label>',
        content
    )
    content = re.sub(
        r'(<input\n\s*type="text"\n\s*value={formData\.path})',
        r'\1 id="path-input"',
        content
    )

    # Fix for Status Code
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">Status Code</label>)',
        r'<label htmlFor="status-code-select" className="block text-sm font-medium mb-1">Status Code</label>',
        content
    )
    content = re.sub(
        r'(<select\n\s*value={formData\.statusCode})',
        r'\1 id="status-code-select"',
        content
    )

    # Fix for Description
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">Description</label>)',
        r'<label htmlFor="description-input" className="block text-sm font-medium mb-1">Description</label>',
        content
    )
    content = re.sub(
        r'(<input\n\s*type="text"\n\s*value={formData\.description})',
        r'\1 id="description-input"',
        content
    )

    # Fix for Response Body
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">\s*Response Body\s*</label>)',
        r'<label htmlFor="response-body-textarea" className="block text-sm font-medium mb-1">Response Body</label>',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'(<textarea\n\s*value={formData\.responseBody})',
        r'\1 id="response-body-textarea"',
        content
    )

    # Fix for Response Headers: we label the div that contains the headers
    content = re.sub(
        r'(<label className="block text-sm font-medium mb-1">\s*Response Headers\s*</label>)',
        r'<label htmlFor="response-headers-div" className="block text-sm font-medium mb-1">Response Headers</label>',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'(<div className="space-y-2">)',
        r'<div id="response-headers-div" className="space-y-2">',
        content
    )

    # Fix for Active
    content = re.sub(
        r'(<label className="text-sm font-medium text-gray-700">Active</label>)',
        r'<label htmlFor="active-checkbox" className="text-sm font-medium text-gray-700">Active</label>',
        content
    )
    content = re.sub(
        r'(<input\n\s*type="checkbox"\n\s*checked={formData\.active})',
        r'\1 id="active-checkbox"',
        content
    )

    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fix_labels.py <filepath>")
        sys.exit(1)
    fix_labels(sys.argv[1])