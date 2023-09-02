import pandas as pd
from typing import Tuple


class ManualTransliterator:
    def __init__(self):
        pass

    @staticmethod
    def generate_coordinates(text: str, max_columns: int = 20) -> pd.DataFrame:
        try:
            paragraphs = text.split("\n\n")  # Split text into paragraphs
            num_paragraphs = len(paragraphs)

            # Create an empty DataFrame
            df = pd.DataFrame()

            for p_idx, paragraph in enumerate(paragraphs):
                words = paragraph.split()
                num_words = len(words)
                num_rows = (num_words + max_columns - 1) // max_columns  # Calculate number of rows needed

                paragraph_df = pd.DataFrame(index=range(num_rows), columns=range(max_columns))

                row = 0
                col = 0
                for idx, word in enumerate(words):
                    # Handle full stop
                    if word.endswith('.'):
                        paragraph_df.at[row, col] = word[:-1]  # Remove the full stop and store in the current cell
                        col += 1  # Move to the next column
                        paragraph_df.at[row, col] = '.'  # Place the full stop in the next cell
                        col += 1  # Move to the next column
                    else:
                        paragraph_df.at[row, col] = word
                        col += 1  # Move to the next column

                    # Check if the maximum column limit is reached
                    if col >= max_columns:
                        row += 1
                        col = 0

                # Reset index of paragraph_df
                paragraph_df.reset_index(drop=True, inplace=True)

                # Concatenate with df
                df = pd.concat([df, paragraph_df], axis=0)

                # Add an empty row between paragraphs
                if p_idx < num_paragraphs - 1:
                    empty_row = pd.Series([None] * max_columns)
                    df = pd.concat([df, pd.DataFrame([empty_row])], axis=0)

                # Reset index of df
                df.reset_index(drop=True, inplace=True)

            return df

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error

    @staticmethod
    def replace_cells(dataframe: pd.DataFrame, replacement_dict: dict) -> Tuple[pd.DataFrame, list]:
        try:
            changes = []  # Nested list to store changes [(row, col), original, changed]

            for key, value in replacement_dict.items():
                row, col = key

                if pd.notna(dataframe.iat[row, col]):
                    original = dataframe.iat[row, col]
                    dataframe.iat[row, col] = value
                    changes.append([(row, col), original, value])

            return dataframe, changes

        except Exception as e:
            print(f"An error occurred in replace_cells: {str(e)}")
            return dataframe, []  # Return the original DataFrame and an empty changes list

    @staticmethod
    def undo_changes(dataframe: pd.DataFrame, changes: list) -> pd.DataFrame:
        try:
            for change in changes:
                (row, col), original, _ = change
                dataframe.iat[row, col] = original

            return dataframe

        except Exception as e:
            print(f"An error occurred in undo_changes: {str(e)}")
            return dataframe  # Return the original DataFrame in case of error

    @staticmethod
    def reconstruct_text(dataframe: pd.DataFrame) -> str:
        try:
            paragraphs = []
            paragraph = []

            # Iterate over each row in the DataFrame
            for _, row in dataframe.iterrows():
                sentence = []
                for col in row:
                    if pd.notna(col):
                        if col == ".":
                            sentence.append(".")
                        else:
                            sentence.append(col)

                if len(sentence) > 0:
                    paragraph.extend(sentence)
                else:
                    if len(paragraph) > 0:
                        paragraphs.append(" ".join(paragraph))
                        paragraph = []

            if len(paragraph) > 0:
                paragraphs.append(" ".join(paragraph))

            # Join paragraphs with double line breaks and replace spaces around full stops
            constructed_text = "\n\n".join(paragraphs)
            constructed_text = constructed_text.replace(" .", ".").replace("\n\n", "\n")
            return constructed_text

        except Exception as e:
            print(f"An error occurred in reconstruct_text: {str(e)}")
            return ""  # Return an empty string in case of error

    @staticmethod
    def to_csv(dataframe: pd.DataFrame, file: str = "dataframe.csv") -> None:
        try:
            # Save the DataFrame to a CSV file
            dataframe.to_csv(file, index=True)
        except Exception as e:
            print(f"An error occurred in to_csv: {str(e)}")

    @staticmethod
    def manual_mask(dataframe: pd.DataFrame, coordinates: list) -> Tuple[str, list]:
        try:
            changes = []  # To store changes [(row, col), original]
            for coord in coordinates:
                row, col = coord
                original_text = dataframe.iat[row, col]  # Get the original text
                changes.append([(row, col), original_text])

                # Mask the specified cell with "<mask>"
                dataframe.iat[row, col] = "<mask>"

            # Use the changes list to undo the masking after reconstruction
            reconstructed_text = ManualTransliterator.reconstruct_text(dataframe=dataframe)
            return reconstructed_text, changes

        except Exception as e:
            print(f"An error occurred in manual_masking: {str(e)}")
            return "", []  # Return an empty string and an empty list in case of error