from trader import call_moxfield_api_sync

def test_call_moxfield_api_sync_returns_expected_json():
    moxfield_id = "Tn1Ta-3HsEKtpGYrJG_d6Q"
    moxfield_type = "collection"

    result = call_moxfield_api_sync(moxfield_id, moxfield_type)
    assert 'data' in result

    first_item = result['data'][0]
    assert 'count' in first_item
    assert 'name' in first_item['card']
    assert 'expansion' in first_item['card']
    assert 'scryfall_id' in first_item['card']
    assert 'cn' in first_item['card']