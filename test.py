from beem import vote
from datetime import datetime, timedelta
import pytz


def test_hivewatchers_votes():
    yesterday = datetime.now() - timedelta(days=1)
    tz = pytz.timezone('US/Eastern')
    start_date = tz.localize(yesterday)
    hivewatchers_votes = vote.AccountVotes('hivewatchers', start=start_date)
    assert len(hivewatchers_votes) > 0, 'No hivewatchers votes'
