def getfact(words, pos_tags, name):
    relationship_nouns = ["father", "mother", "son", "relative", "relatives", "friend", "friends"]
    noun_tags = ['NN', 'NNS', 'NNP', 'NNPS']

    current_relationship = next((word.lower() for word in words if word.lower() in relationship_nouns), None)
    final_relationship = ""
    entities = []

    if current_relationship:
        if current_relationship in ["father", "mother"]:
            final_relationship = "son_of"
        elif current_relationship in ["friend", "friends"]:
            final_relationship = "are_friends"
        elif current_relationship in ["relative", "relatives"]:
            final_relationship = "are_relatives"
        elif current_relationship == "son":
            final_relationship = "son_of"

        if pos_tags[0][0] == "My" or pos_tags[0][0] == 'I' or words[0] in name:
            entities.append(name)
            relevant_nouns = [word for word, tag in pos_tags if word not in relationship_nouns and tag in noun_tags]
            entities.append(relevant_nouns[1])
        else:
            relevant_nouns = [word for word, tag in pos_tags if word not in relationship_nouns and tag in noun_tags]
            entities = relevant_nouns[:2]
        if final_relationship == "son_of" and "my" not in words and "of" in words and words.index(current_relationship) + 1 < len(words):
            entities[0], entities[1] = entities[1], entities[0]

    if final_relationship and len(entities) > 0:
        if len(entities) == 1:
            entities.extend([name, entities[0]])
        relationship_string = f"{final_relationship}({entities[0]},{entities[1]})"
        entities.extend([final_relationship, relationship_string])

    return entities