import pandas as pd
from loader import load_data
from preprocess import preprocess_dataframe

COOPERATION_WORDS = {
    "collaborate": 2,
    "cooperate": 2,
    "cooperation": 2,
    "together": 1,
    "partnership": 3,
    "consensus": 3,
    "joint": 2,
    "support": 2,
    "unity": 3,
    "alliance": 3,

    "mutual": 2,
    "shared": 1,
    "collective": 2,
    "teamwork": 2,
    "coordination": 2,

    "compromise": 2,
    "reconcile": 2,
    "harmonize": 2,
    "align": 2,
    "integrate": 2,

    "solidarity": 3,
    "synergy": 2,
    "coalition": 3,
    "assist": 1,
    "contribute": 1,

    "engage": 1,
    "participate": 1,
    "work with": 2,
    "build together": 2,
    "multilateral": 3,

    "dialogue": 2,
    "engagement": 2,
    "diplomacy": 3
}

ASSERTIVE_WORDS = {
    "must": 4,
    "strongly": 2,
    "firmly": 3,
    "cannot": 4,
    "never": 4,

    "demand": 4,
    "reject": 3,
    "insist": 3,
    "require": 3,
    "compel": 4,

    "undeniable": 3,
    "certainly": 2,
    "clearly": 2,
    "obviously": 2,

    "without question": 4,
    "no doubt": 3,
    "absolutely": 4,
    "decisively": 3,

    "categorically": 4,
    "definitely": 2,
    "refuse": 3,
    "prohibit": 4,

    "mandate": 4,
    "enforce": 4,
    "guarantee": 3,
    "will not": 4,

    "shall": 3,
    "ought": 2,
    "unacceptable": 4,
    "nonnegotiable": 4,
    "urge": 2,
    "strictly": 3
}

SUPPORT_WORDS = {
    "support": 2,
    "approve": 2,
    "agreement": 1,
    "agree": 1,
    "favour": 1,

    "yes": 1,
    "accept": 1,
    "endorse": 3,
    "back": 2,
    "advocate": 3,

    "champion": 4,
    "uphold": 3,
    "validate": 2,
    "confirm": 2,

    "encourage": 1,
    "recommend": 1,
    "promote": 2,
    "defend": 3,

    "stand with": 3,
    "in favor": 1,
    "positive": 1,
    "beneficial": 1,

    "constructive": 1,
    "helpful": 1,
    "backing": 2,
    "ratify": 3,
    "welcome": 1,
    "appreciate": 1,

    "commend": 2,
    "align": 2,
    "reinforce": 3,
    "strengthen": 3
}

OPPOSE_WORDS = {
    "oppose": 3,
    "reject": 3,
    "disagree": 2,
    "deny": 3,

    "no": 2,
    "against": 2,
    "object": 2,
    "resist": 3,

    "criticize": 2,
    "condemn": 4,
    "challenge": 2,
    "counter": 2,

    "refute": 3,
    "dismiss": 3,
    "contradict": 2,
    "protest": 3,

    "block": 4,
    "prevent": 3,
    "veto": 4,
    "disapprove": 2,

    "negative": 1,
    "harmful": 2,
    "detrimental": 3,

    "flawed": 2,
    "problematic": 2,
    "inaccurate": 2,

    "question": 1,
    "undermine": 3,
    "boycott": 4,

    "concern": 1,
    "doubt": 1,
    "unacceptable": 4,
    "nonnegotiable": 4
}


def calculate_text_len(words):
    return len(words.split())

def calculate_cooperation_words(words):
    len_words = len(words.split())
    if len_words == 0:
        return 0
    
    c_words = 0
    for word in words.split():
        if word in COOPERATION_WORDS:
            c_words += COOPERATION_WORDS[word]
    
    cooperation_words = c_words / len_words
    return cooperation_words

def calculate_assertive_words(words):
    len_words = len(words.split())
    if len_words == 0:
        return 0
    
    a_words = 0
    for word in words.split():
        if word in ASSERTIVE_WORDS:
            a_words += ASSERTIVE_WORDS[word]
    
    assertive_words = a_words / len_words
    return assertive_words

def calculate_support_words(words):
    len_words = len(words.split())
    if len_words == 0:
        return 0
    
    s_words = 0
    for word in words.split():
        if word in SUPPORT_WORDS:
            s_words += SUPPORT_WORDS[word]

    support_words = s_words / len_words
    return support_words

def calculate_oppose_words(words):
    len_words = len(words.split())
    if len_words == 0:
        return 0
    
    o_words = 0
    for word in words.split():
        if word in OPPOSE_WORDS:
            o_words += OPPOSE_WORDS[word]
    
    oppose_words = o_words / len_words
    return oppose_words

def calculate_stance_score(words):
    positive = calculate_support_words(words)
    negative = calculate_oppose_words(words)
    print(positive, negative)
    stance_score = (positive - negative)/(positive + negative + 0.0000001)
    return stance_score


def add_features(df):
    
    df["Coorporative_Index"] = df["clean_speech"].apply(calculate_cooperation_words)
    df["Assertive_Index"] = df["clean_speech"].apply(calculate_assertive_words)
    df["stance_score"] = df["clean_speech"].apply(calculate_stance_score)
    df["text_length"] = df["clean_speech"].apply(calculate_text_len)

    
    return df