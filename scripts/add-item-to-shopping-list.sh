ITEM_TO_ADD="$*"

#echo "adding ${ITEM_TO_ADD}"

if [ ! -z "$ITEM_TO_ADD" ] ; then

curl -X PATCH 'https://api.notion.com/v1/blocks/92d98ac3dc86460285a399c0b1176fc5/children' \
  -H 'Authorization: Bearer '"$NOTION_SHOPPING_LIST_KEY"'' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-02-22" \
  --data '{
	"children": [
		{
			"object": "block",
			"type": "to_do",
			"to_do": {
				"rich_text": [
        { "type": "text", "text": { "content": "'"$ITEM_TO_ADD"'" } }
        ],
        "checked": false
			}
    }
	]
}'

fi
