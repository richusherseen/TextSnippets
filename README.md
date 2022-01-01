# TextSnippets


this is atext saving and retrieval web app using Django. This app can save short text snippets with a title, timestamp and created user. The snippet contain a relation to a Tag model (simple model with only title field). Tag title is unique. it will not create tags for every snippet, check whether the tag with the same title exists or not before creating a new one. If the same tag exists link to that tag.It uses JWT authentication for getting user.
