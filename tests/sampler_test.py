from mentat.conversation import MentatAssistantMessageParam
from mentat.parsers.parser import ParsedLLMResponse
            MentatAssistantMessageParam(
                parsed_llm_response=ParsedLLMResponse("", "test_assistant_content", []),
    sampler.set_active_diff()
    assert remove_checksums(sample.diff_active) == remove_checksums(expected_diff)
    assert sample.message_history == []
    assert sample.message_prompt == "test_user_content"
    assert sample.message_edit == "test_assistant_content"
    assert sample.context == ["multifile_calculator/operations.py"]
    assert sample.diff_edit == ""
    assert sample.version == "0.2.0"
    parsedLLMResponse = GitParser().parse_llm_response(test_sample["diff_edit"])
    sample.version = "2.3"
    parsedLLMResponse = GitParser().parse_llm_response(diff_edit)
    assert sample.message_edit == "I will make the following edits."