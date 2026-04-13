import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.getcwd())

from logger import *   # sets up file + console logging
import logging

from src.Coder_Buddy.pipelines.CodeWriterLoop_pipeline import CodeWriterLoopPipeline

import asyncio


async def main():
    try:
        # ── File paths ────────────────────────────────────────────
        base_path = os.path.join(os.getcwd(), 'public')
        html_file_path = os.path.join(base_path, 'index.html')
        js_file_path   = os.path.join(base_path, 'scripts/script.js')
        css_file_path  = os.path.join(base_path, 'styles/style.css')

        logging.info("=" * 60)
        logging.info("  CodeWriterLoop Pipeline — starting")
        logging.info("=" * 60)
        logging.debug(f"HTML : {html_file_path}")
        logging.debug(f"JS   : {js_file_path}")
        logging.debug(f"CSS  : {css_file_path}")

        # ── Existence check ───────────────────────────────────────
        for path, label in [
            (html_file_path, 'HTML'),
            (js_file_path,   'JS'),
            (css_file_path,  'CSS'),
        ]:
            if os.path.exists(path):
                logging.info(f"  ✓ {label} file found: {path}")
            else:
                logging.warning(f"  ✗ {label} file NOT found: {path}")

        # ── Pipeline init ─────────────────────────────────────────
        pipeline = CodeWriterLoopPipeline()
        logging.info("CodeWriterLoopPipeline initialised")

        prompt = "The app is not working — analyse the code and fix all bugs"
        logging.info(f"Prompt: {prompt!r}")

        # ── Run pipeline ──────────────────────────────────────────
        result = await pipeline.initiate(
            prompt=prompt,
            html_file_path=html_file_path,
            js_file_path=js_file_path,
            css_file_path=css_file_path,
        )

        logging.info("=" * 60)
        logging.info("  Pipeline finished successfully ✓")
        logging.info(f"  Result: {result}")
        logging.info("=" * 60)

    except Exception as e:
        logging.error(f"✗ Pipeline test failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    asyncio.run(main())