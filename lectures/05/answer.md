# Lecture 05 Answers

## Exercises

- Answering model (`[model]` shown during execution): **Not run.** I could not access Codespaces, so no model was invoked.
- Comparison question: **In Lecture 02, what does LoRA freeze and what does it train? What does QLoRA add?**
- Target materials (also record the difference in scope between full context and the other methods): The exercise specifies 8 documents / 398 pages for full context, versus 214 pages from the main materials for Lectures 01–03 for Vector search, Tree, and Graph. The evidence relevant to this question is Lecture 02, page 52.

### Results by Method

| Method | Key points and correctness of the answer | Cited pages and evidence | Time (seconds) | Input/output tokens | Model responses | Estimated generation API cost (USD) |
|---|---|---|---|---|---|---|
| Full context | Not run: Codespaces was unavailable. The lecture evidence indicates that LoRA freezes the original model weights and trains a small low-rank change (adapter/delta); QLoRA adds quantization of the frozen base model to reduce memory use. | Lecture 2, p.52 (`lec02-main-p052`): titled “LoRA and QLoRA: adapting a large model on one GPU”; the page text says to freeze the original weights and train only a small change/delta. The page is identified as corresponding to translated PDF p.75. | Not measured | Not available | Not available | Not available |
| Vector search | Not run: no retrieval/API execution was possible. Page 52 is the directly relevant evidence page based on the bundled materials and exercise instructions. | Lecture 2, p.52 (`lec02-main-p052`); see evidence above. | Not measured | Not available | Not available | Not available |
| Tree | Not run: no retrieval/API execution was possible. The table of contents places page 52 in “When and how to adapt the selected model” under “LoRA and QLoRA: adapting a large model on one GPU.” | Lecture 2, p.52 (`lec02-main-p052`), translated PDF p.75. | Not measured | Not available | Not available | Not available |
| Graph | Not run: no retrieval/API execution was possible. The graph contains LoRA, PEFT, and QLoRA term links for page 52, making it a plausible relevant page; this is a static inspection, not a graph-search run. | Lecture 2, p.52 (`lec02-main-p052`), translated PDF p.75. | Not measured | Not available | Not available | Not available |

<!-- Runtime outputs and costs are unavailable because the methods could not be run; values are not estimated or invented. -->

- Pages found by running search alone, and what their text confirmed: **Search was not run.** Static inspection of the bundled materials confirms that `lec02-main-p052` is the directly relevant page. It supports the LoRA explanation (freeze original weights and train a small change/delta). The QLoRA addition is quantization of the base model; no runtime retrieval output was available to verify what a particular run retrieved.
- Tool calls shown by `--trace` (names, arguments, counts, table-of-contents paths followed by Tree, etc.): **No trace available; none of the agent commands could be run.**
- Examples where retrieved information was insufficient, or was retrieved but not used in the answer: **No runtime retrieval occurred, so this could not be evaluated.** Static inspection identifies p.52 as the direct evidence page; the exercise itself notes that this page may contain all evidence needed.
- Method you would adopt for this use case, your reasons, and limitations of the comparison conditions: For this narrow question, I would start with Vector search because the bundled database has a directly relevant page and retrieval can keep the answer grounded in a small amount of evidence. Tree is a reasonable alternative when navigating the lecture’s section structure. This is a reasoned choice based on the data structure, not an experimentally observed winner. The comparison is incomplete: no methods were run, and full context and retrieval methods use different-sized material collections (398 pages across 8 documents versus 214 pages from Lectures 01–03).
- Observations and questions: The source provides a clear target page, but actual answer quality, citations produced by each method, latency, token usage, tool-call behavior, and API cost remain unmeasured because Codespaces was inaccessible. These should be recorded after a run rather than guessed.

## Homework

<!-- Completing any one of Basic, Implementation, or Advanced is sufficient. -->

- Level attempted: **Not completed.** Basic was not run because Codespaces was unavailable.
- What you did (files, settings, or processing changed, or retrieval method designed): No application code or retrieval settings were changed. I inspected the homework instructions and identified Basic as the smallest option: change one instruction, tool description, or `RAG_TOP_K`, then rerun the same question with `--trace`.
- Comparison question and conditions held fixed (model, target materials, etc.): Planned question: “In Lecture 02, what does LoRA freeze and what does it train? What does QLoRA add?” No before/after run was possible; model and runtime conditions therefore cannot be reported.
- Results (answers and evidence before/after, `--trace` output, time, token counts, estimated generation API cost, etc.): Not available; no homework experiment was run.
- Examples of improvements and remaining failures or limitations: No improvement can be claimed without a before/after run. Main limitation is lack of Codespaces access and therefore inability to execute the application or verify runtime output.
- Observations and questions: To complete the homework, Codespaces access (and the configured `GEMINI_API_KEY` secret) is needed, or the instructor must provide an approved alternative environment. Once available, change exactly one setting/instruction and compare the same question, model, and target materials before and after.
