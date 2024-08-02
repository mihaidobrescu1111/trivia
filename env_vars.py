import os

# HOW MUCH TIME USERS HAVE TO ANSWER THE QUESTION? IN PROD WILL PROBABLY BE 18 or 20.
QUESTION_COUNTDOWN_SEC = int(os.environ.get("QUESTION_COUNTDOWN_SEC", 22))
        
# NUMBER OF SECONDS TO KEEP THE FAILED TOPIC IN THE UI (USER INTERFACE) BEFORE REMOVING IT FROM THE LIST
KEEP_FAILED_TOPIC_SEC = int(os.environ.get("KEEP_FAILED_TOPIC_SEC", 5))
        
# DON'T ALLOW USER TO WRITE LONG TOPICS
MAX_TOPIC_LENGTH_CHARS = int(os.environ.get("MAX_TOPIC_LENGTH_CHARS", 30))
    
# AUTOMATICALLY ADD TOPICS IF THE USERS DON'T BID/PROPOSE NEW ONES
MAX_NR_TOPICS_FOR_ALLOW_MORE = int(os.environ.get("MAX_NR_TOPICS_FOR_ALLOW_MORE", 20))

# NUMBER OF TOPICS TO APPEAR IN THE UI. THE ACTUAL LIST CAN CONTAIN MORE THAN THIS.
NR_TOPICS_TO_BROADCAST = int(os.environ.get("NR_TOPICS_TO_BROADCAST", 5))

# MINIMUM NUMBER OF POINTS REQUIRED TO PLACE A TOPIC BID IN THE UI
BID_MIN_POINTS = int(os.environ.get("BID_MIN_POINTS", 3))
    
# MAX LENGTH OF THE USER PROVIDED TOPIC (WE REDUCE MALICIOUS INPUT)
TOPIC_MAX_LENGTH = int(os.environ.get("TOPIC_MAX_LENGTH", 25))
    
DUPLICATE_TOPIC_THRESHOLD = float(os.environ.get("DUPLICATE_TOPIC_THRESHOLD", 0.9))

#How many consecutive question does a user have to answer in order to win combo points?
COMBO_CONSECUTIVE_NR_FOR_WIN = int(os.environ.get("COMBO_CONSECUTIVE_NR_FOR_WIN", 3))

#How many points does a combo bonus offer?
COMBO_WIN_POINTS = int(os.environ.get("COMBO_WIN_POINTS", 50))

HF_CLIENT_ID = os.environ.get("HF_CLIENT_ID")
HF_CLIENT_SECRET = os.environ.get("HF_CLIENT_SECRET")
HF_REDIRECT_URI = os.environ.get("HF_REDIRECT_URI")

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.environ.get("GOOGLE_REDIRECT_URI")

DB_DIRECTORY = os.environ.get("DB_DIRECTORY", "")