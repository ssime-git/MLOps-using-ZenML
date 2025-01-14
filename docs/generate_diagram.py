import requests
import os

def generate_mermaid_diagram():
    # Read the Mermaid diagram definition
    with open('docs/architecture.md', 'r') as f:
        content = f.read()
    
    # Extract the Mermaid diagram part
    mermaid_part = content.split('```mermaid\n')[1].split('```')[0]
    
    # Mermaid Live Editor API
    url = "https://mermaid.ink/img/pako:"
    
    # Convert diagram to base64
    import base64
    import zlib
    
    compressed = zlib.compress(mermaid_part.encode('utf-8'))
    b64 = base64.b64encode(compressed).decode('utf-8')
    
    # Generate the URL
    full_url = f"{url}{b64}"
    
    # Download the image
    response = requests.get(full_url)
    if response.status_code == 200:
        with open('docs/architecture.png', 'wb') as f:
            f.write(response.content)
        print("Architecture diagram generated successfully!")
    else:
        print(f"Error generating diagram: {response.status_code}")

if __name__ == "__main__":
    generate_mermaid_diagram()
