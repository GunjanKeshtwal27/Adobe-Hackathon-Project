class OutlineGenerator:
    def __init__(self):
        """
        Initializes the OutlineGenerator.
        Font sizes for title and headings will be determined dynamically.
        """
        self.title_size = 0
        self.h1_size = 0
        self.h2_size = 0
        self.h3_size = 0

    def _analyze_font_sizes(self, extracted_data):
        """
        Analyzes font sizes to identify potential font sizes for headings.
        This is a heuristic approach and can be refined further.
        """
        size_counts = {}
        for item in extracted_data:
            size = item["font_size"]
            size_counts[size] = size_counts.get(size, 0) + 1

        # Sort font sizes in descending order to identify potential heading sizes.
        # This is a simplified assumption; real-world PDFs might require more sophisticated logic.
        sorted_sizes = sorted(size_counts.keys(), reverse=True)

        # Assign the largest sizes to Title, H1, H2, H3 respectively.
        # This assumes a clear hierarchy in font sizes.
        if len(sorted_sizes) > 0:
            self.title_size = sorted_sizes[0]
        if len(sorted_sizes) > 1:
            self.h1_size = sorted_sizes[1]
        if len(sorted_sizes) > 2:
            self.h2_size = sorted_sizes[2]
        if len(sorted_sizes) > 3:
            self.h3_size = sorted_sizes[3]

        print(f"Detected font sizes: Title={self.title_size}, H1={self.h1_size}, H2={self.h2_size}, H3={self.h3_size}")


    def generate_outline(self, extracted_data):
        """
        Generates a structured outline (title and headings) from the extracted data.
        """
        self._analyze_font_sizes(extracted_data)

        title = ""
        outline = []
        
        # Identify the title (typically the largest font and within the first few lines)
        for i, item in enumerate(extracted_data):
            if item["font_size"] == self.title_size and i < 5: # Look for title within the first 5 items
                title = item["text"]
                break

        # Identify headings based on font size and boldness
        for item in extracted_data:
            level = None
            if item["font_size"] == self.h1_size and item["is_bold"]:
                level = "H1"
            elif item["font_size"] == self.h2_size and item["is_bold"]:
                level = "H2"
            elif item["font_size"] == self.h3_size and item["is_bold"]:
                level = "H3"
            
            # If no heading level is determined by font size,
            # try to infer based on boldness and text length.
            # This is a fallback heuristic and can be improved.
            if level is None and item["is_bold"] and len(item["text"]) < 100: # Avoid treating very long text as heading
                # Here, you could add more sophisticated logic, such as text position,
                # or its size relative to other headings.
                # For now, we'll consider it H3 if it's bold and relatively short,
                # and its font size is greater than the determined H3 size (to catch variations).
                if item["font_size"] > self.h3_size: 
                    level = "H3"


            if level:
                outline.append({
                    "level": level,
                    "text": item["text"],
                    "page": item["page"]
                })
        
        # Remove duplicate headings (if the same heading was extracted multiple times)
        unique_outline = []
        seen_headings = set()
        for entry in outline:
            key = (entry["level"], entry["text"])
            if key not in seen_headings:
                unique_outline.append(entry)
                seen_headings.add(key)

        return {"title": title, "outline": unique_outline}

