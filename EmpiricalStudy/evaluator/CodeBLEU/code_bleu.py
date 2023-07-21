# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.

# -*- coding:utf-8 -*-
import bleu
import weighted_ngram_match
import syntax_match
import dataflow_match


def _code_bleu_single_sentence(ref, hyp, lang):
    alpha, beta, gamma, theta = 0.25, 0.25, 0.25, 0.25
    tok_ref = [[ref.strip().split()]]
    tok_hyp = [hyp.strip().split()]

    ngram_match_score = bleu.corpus_bleu(tok_ref, tok_hyp)
    keywords = [x.strip() for x in open('keywords/' + lang + '.txt', 'r', encoding='utf-8').readlines()]

    def make_weights(reference_tokens, key_word_list):
        return {token: 1 if token in key_word_list else 0.2 for token in reference_tokens}

    ref_with_weights = [[[ref_tokens, make_weights(ref_tokens, keywords)] for ref_tokens in ref0] for ref0 in tok_ref]
    weighted_ngram_match_score = weighted_ngram_match.corpus_bleu(ref_with_weights, tok_hyp)
    syntax_match_score = syntax_match.corpus_syntax_match([[ref]], [hyp], lang)
    dataflow_match_score = dataflow_match.corpus_dataflow_match([[ref]], [hyp], lang)
    if dataflow_match_score == 0:
        dataflow_match_score = 1
    # print(
    #     'ngram match: {0}, weighted ngram match: {1}, syntax_match: {2}, dataflow_match: {3}'.
    #     format(ngram_match_score,
    #            weighted_ngram_match_score,
    #            syntax_match_score,
    #            dataflow_match_score))

    code_bleu_score = alpha * ngram_match_score + beta * weighted_ngram_match_score \
                      + gamma * syntax_match_score + theta * dataflow_match_score

    return code_bleu_score
