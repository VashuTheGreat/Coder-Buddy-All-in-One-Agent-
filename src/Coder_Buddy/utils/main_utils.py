import logging
import os
from exception import MyException
import sys
from src.Coder_Buddy.models.file_code_writer_model import File_to_change


async def update_file_by_line_update(file_path: str, changes: File_to_change) -> None:
    """
    Applies line-level edits to a file on disk.

    Line numbers are 0-based (as the LLM returns them):
      - line_number=0  → first line of the file
      - line_number >= len(lines) → append new lines at the end

    Changes are applied in sorted order so appends are sequential.
    """
    try:
        if not os.path.exists(file_path):
            logging.warning(
                f"update_file_by_line_update: file does not exist, will create it → {file_path}"
            )
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            open(file_path, 'w').close()   # create empty file

        # Read current lines
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        original_len = len(lines)
        logging.debug(
            f"update_file_by_line_update: '{os.path.basename(file_path)}' "
            f"— {original_len} lines, {len(changes.changes)} change(s)"
        )

        # Sort by line_number so appends are written in order
        sorted_changes = sorted(changes.changes, key=lambda c: c.line_number)

        for change in sorted_changes:
            idx = change.line_number          # 0-based index
            new_content = change.new_line
            if not new_content.endswith('\n'):
                new_content += '\n'

            if 0 <= idx < len(lines):
                # In-range: replace existing line
                logging.debug(
                    f"  [line {idx}] replace: {lines[idx].rstrip()!r} → {change.new_line!r}"
                )
                lines[idx] = new_content

            elif idx >= len(lines):
                # Out-of-range: append, filling any gap with blank lines
                while len(lines) < idx:
                    lines.append('\n')
                logging.debug(f"  [line {idx}] append: {change.new_line!r}")
                lines.append(new_content)

            else:
                # Negative index — skip (shouldn't happen with 0-based LLM output)
                logging.warning(f"  [line {idx}] negative index — skipping")

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        logging.info(
            f"  ✓ '{os.path.basename(file_path)}' updated "
            f"({original_len} → {len(lines)} lines)"
        )

    except Exception as e:
        logging.error(
            f"update_file_by_line_update failed for {file_path}: {e}", exc_info=True
        )
        raise MyException(e, sys)
