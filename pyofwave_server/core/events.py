"""
Standard detectors for events.

Does not include:
- events that are difficult to detect in this way (WAVELET_TAGS_CHANGED, WAVELET_TITLE_CHANGED).

To use, call getEvents(delta, manifast) for each delta
and getTrue(participants, doc.participantsChanged, user) once.
Parameters can easily be retrieved once you've got events.
"""

import datasource as ds

wavelet = { # pass these these the delta for the wavelet.
    "WAVELET_BLIP_CREATED" : lambda wavelet:"blip" in wavelet,
    "WAVELET_BLIP_REMOVED" : lambda wavelet:"!!-blip" in wavelet
    }

participants = { # pass these the current wavelet delta and user object
    "WAVELET_PARTICIPANTS_CHANGED" : lambda participants, user: True,
    "WAVELET_SELF_ADDED" : lambda participants, user: user.address in participants,
    "WAVELET_SELF_REMOVED" : lambda participants, user: "!"+user.address in participants,
    }

blip = { # pass these a blip delta.
    "BLIP_CONTRIBUTORS_CHANGED" : lambda blip: "contributor" in blip or "!!-contributor" in blip,
    "BLIP_SUBMITTED" : lambda blip: True,
    "FORM_BUTTON_CLICKED" : lambda blip: ds.Item(ds.Item.TYPE_START_TAG, "input", type="button", checked="1") in blip
    "ANNOTATED_TEXT_CHANGED" : lambda blip: ds.Item(ds.Item.TYPE_TEXT, "") in blip
}

docTypes = { # use to determine other dictionary to use, pass document ID and root wavelet
    "wavelet" : lambda docID, manifast: manifast.id == docID,
    "blip" : lambda docID, manifast: ds.Item(ds.Item.TYPE_START_TAG, "blip", id=docID) in manifast,
    "peer" : lambda docID, manifast: ds.Item(ds.Item.TYPE_START_TAG, "peer", id=docID) in manifast
    }

dictionaries = {
    "wavelet" : wavelet,
    "blip" : blip,
    "peer" : {
        "GADGET_STATE_CHANGED" : lambda doc: True,
        },
}

def getTrue(diction, *args):
    res = []
    for key in diction.keys():
        if diction[key](*args): res.append(key)

    return res

def getEvents(delta, manifast):
    import tags
    tag = tags.TagDelta(delta)

    return getTrue(dictionaries[getTrue(docTypes, delta.doc.id, manifast)[0]], tag)

    
