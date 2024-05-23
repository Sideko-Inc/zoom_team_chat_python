
# Zoom Team Chat Python SDK

## Overview
Connect your teams and streamline communications with instant messaging integrated into the Zoom platform

## Authentication
Use either the synchronous or asynchronous client to authenticate 

### Synchronous Client
```python
from zoom_team_chat import Client
from os import getenv

Client(token=getenv("API_TOKEN"))
```

### Asynchronous Client
```python
from zoom_team_chat import AsyncClient
from os import getenv

AsyncClient(token=getenv("API_TOKEN"))
```


### Delete a channel
> Deletes a specific channel. Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate via chat in private or public groups. 



**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:delete:channel`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.channel.delete(channel_id="825c9e31f1064c73b394c5e4557d3447")
```

---

### Batch remove members from a channel
> Removes multiple members from a chat channel in a batch. A [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) can have one or many members.   
   
 
 

**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:delete:batch_members`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.channel.member.batch_delete(
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    member_ids="zqmgs2tmspguoqcxyahsya,R4VM29Oj0fVM2hhEmSKVM2hhezJTezJTKVM2hezJT2hezJ",
    user_ids="zqmgs2tmspguoqcxyahsya,R4VM29Oj0fVM2hhEmSKVM2hhezJTezJTKVM2hezJT2hezJ",
)
```

---

### Remove a member (group)
> Removes a group from a chat channel.

**Scopes:** `chat_channel:write:admin`

**Granular Scopes:** `team_chat:delete:group:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.member.group.delete(
    channel_id="825c9e31f1064c73b394c5e4557d3447", group_id="abc"
)
```

---

### Leave a channel
> Leaves a specific channel. If you're no longer interested in being a member of an existing channel, you can leave the channel at any time. After leaving the channel, you can no longer access information from that channel.

**Note:** This API only supports **user-managed** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app)


**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:delete:member`,`team_chat:delete:member:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.member.me.leave(channel_id="825c9e31f1064c73b394c5e4557d3447")
```

---

### Remove a member
>  Removes a member from a chat channel. A [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) can have one or many members.   
   
 
 

**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:delete:member`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.channel.member.delete(
    channel_id="825c9e31f1064c73b394c5e4557d3447", identifier="jchill@example\.com"
)
```

---

### Delete a custom emoji
> Delete a custom emoji by *fileId*.

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:delete:custom_emoji`,`team_chat:delete:custom_emoji:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.emoji.delete(file_id="qgH9UN5YSsuBEMuKBHs34Q")
```

---

### Delete a chat file
> Deletes a chat file.

**Scopes:** `chat:write`

**Granular Scopes:** `team_chat:delete:file`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.file.delete(file_id="LDG2jzoOS2aV4wkyLMaryg")
```

---

### Delete legal hold matters
> Deletes a legal hold matter.

**Scopes:** `chat_history_legal_hold:write:admin`

**Granular Scopes:** `team_chat:delete:legal_hold_matter:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.legalhold.matter.delete(
    matter_id="28c92682\-f4fc\-47b0\-bceb\-14cb839e0279"
)
```

---

### Delete a scheduled message
> Deletes a scheduled message.

**Scopes:** `chat_message:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.message.schedule.delete(
    draft_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    to_channel="825c9e31f1064c73b394c5e4557d3447",
    to_contact="nldhy1xwqwkwgwdlgry2rq",
)
```

---

### Delete a reminder for a message
> Deletes a reminder. 
You must provide one of the following query parameters:
- `to_contact` — The email address of the Zoom contact that you want to delete the reminder.
- `to_channel` — The ID of the Zoom channel where you want to delete the reminder.

**Scopes:** `chat_message:write:admin`,`chat_message:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.message.reminder.delete(
    message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    to_channel="cd102f7602c6428db0a273e632eb020B",
    to_contact="test@example\.com",
)
```

---

### Delete a shared space
> Deletes a shared space. This API endpoint works for user-level and account-level apps.

**Note:** For user-level apps, the user calling this API must be the shared space owner. 
**Note:** For account-level apps, the user calling this API must have a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **Edit** permission for the **Chat Channels** feature.

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:delete:shared_space`,`team_chat:delete:shared_space:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `RESOURCE-INTENSIVE`

```python
client.chat.space.delete(space_id="8609fdea87b44e2f8e0")
```

---

### Demote shared space administrators to members
> Demotes shared space administrators to members. 

**Note:** This API supports account-level apps. The user calling this API must have a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **Edit** permission for the **Chat Channels** feature.

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:delete:shared_space_administrators`,`team_chat:delete:shared_space_administrators:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.admin.demote(
    space_id="8609fdea87b44e2f8e0",
    identifiers="zqmgs2tmspguoqcxyahsya,R4VM29Oj0fVM2hhEmSKVM2hhezJTezJTKVM2hezJT2hezJ",
)
```

---

### Remove members from a shared space
> Removes members from a shared space. 

**Note:** This API supports account-level apps. The user calling this API must have a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **Edit** permission for the **Chat Channels** feature.

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:delete:shared_space_members`,`team_chat:delete:shared_space_members:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.channel.member.delete(
    space_id="8609fdea87b44e2f8e0",
    identifiers="zqmgs2tmspguoqcxyahsya,R4VM29Oj0fVM2hhEmSKVM2hhezJTezJTKVM2hezJT2hezJ",
)
```

---

### Batch delete channels
> Delete channels in batches. For user-level apps, pass the `me` value instead of the `userId` parameter.



**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:delete:channels`,`team_chat:delete:channels:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.user.channel.batch_delete(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    channel_ids="825c9e31f1064c73b394c5e4557d3447,4n5c9t31f1064c787f394c5enng7d3553",
)
```

---

### Delete a channel
> Deletes a specific channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate via chat in private or public groups.



**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:delete:user_channel`,`team_chat:delete:user_channel:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.user.channel.delete(
    user_id="v4iyWT1LTfy8QvPG4GTvdg", channel_id="825c9e31f1064c73b394c5e4557d3447"
)
```

---

### Batch demote channel administrators
> Demotes administrators in a channel in batch. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.



**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:delete:batch_administrators:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.user.channel.admin.demote(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    admin_ids="zqmgs2tmspguoqcxyahsya,za7AvP7o9AxypYwpaKYsOJ2K3VwXBZn4JtxgPGk8Lf7_1w",
    user_ids="zqmgs2tmspguoqcxyahsya,R4VM29Oj0fVM2hhEmSKVM2hhezJTezJTKVM2hezJT2hezJ",
)
```

---

### Remove a member
>  Removes a member from a chat channel. A [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) can have one or many members.  For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.



**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:delete:member:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.user.channel.member.delete(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    identifier="jchill@example\.com",
)
```

---

### Delete a message
> Deletes a chat message previously sent to a contact or a channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter. 

 For an [account-level OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app), this API can only be used on behalf of a user who is assigned with a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **Edit** permission for **Chat Messages**. 

 

**Scopes:** `chat_message:write`,`chat_message:write:admin`

**Granular Scopes:** `team_chat:delete:user_message`,`team_chat:delete:user_message:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.user.message.delete(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    to_channel="825c9e31f1064c73b394c5e4557d3447",
    to_contact="jchill@example\.com",
)
```

---

### Delete an IM directory group
> Delete an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.  
   
 
Scopes: `imgroup:write:admin`  
 
 
 

**Scopes:** `imgroup:write:admin`

**Granular Scopes:** `contact_group:delete:group:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

```python
client.im.group.delete(group_id="SobVexyrQjqCkcxjpBWi6w")
```

---

### Delete IM directory group member
> Delete a member from an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under an account.  
   
 
Scopes: `imgroup:write:admin`  
 
 
 

**Scopes:** `imgroup:write:admin`

**Granular Scopes:** `contact_group:delete:member:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

```python
client.im.group.member.delete(
    group_id="SobVexyrQjqCkcxjpBWi6w", member_id="v4iyWT1LTfy8QvPG4GTvdg"
)
```

---

### List account's public channels
> Lists public chat channels that the account's users create. 

 **Note:** This API only supports account-level apps. The user calling this API must have a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **View** or **Edit** permission for the **Chat Channels** feature.

**Scopes:** `chat_channel:read:admin`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:read:list_channels:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.list(
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42", page_size=10
)
```

---

### Get a channel
> Returns information about a specific channel.

Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate through chat in private or public groups. 

The [**Get a channel**](/docs/api-reference/chat/methods#operation/getChannel) API retrieves the channel information of other account users.

**Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:read:channel`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.get(channel_id="825c9e31f1064c73b394c5e4557d3447")
```

---

### List channel members
> Lists all members of a channel.



**Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:read:list_members`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.channel.member.list(
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
)
```

---

### List channel members (Groups)
> Returns a list of channel member groups.

**Scopes:** `chat_channel:read:admin`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:read:list_groups:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.member.group.list(channel_id="825c9e31f1064c73b394c5e4557d3447")
```

---

### List pinned history messages of channel
> Returns a list of pinned history messages of channel.

**Scopes:** `chat:read`,`chat:read:admin`,`chat:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.channel.pinned.list(
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    include_history=False,
    next_page_token="1707034615202",
    page_size=10,
)
```

---

### Get retention policy of a channel
> Returns the retention policy of a channel.  

**Note:** This API only supports account-level apps. The user calling this API must have a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **View** or **Edit** permission for the **Chat Channels** feature.

**Scopes:** `chat_channel:read:admin`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:read:retention:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.retention.get(channel_id="825c9e31f1064c73b394c5e4557d3447")
```

---

### List custom emojis
> Queries the custom emojis list.

**Scopes:** `chat:read:admin`,`chat:read`,`chat:write:admin`,`chat:write`

**Granular Scopes:** `team_chat:read:list_custom_emojis`,`team_chat:read:list_custom_emojis:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.emoji.list(
    next_page_token="32\.0,\-9223372036854775808,1704438757798,so6Q0cltRtiHe7w_5lM39Q",
    page_size=10,
    search_key="hello",
)
```

---

### Get file info
> Returns information about the chat file.

**Scopes:** `chat:read`

**Granular Scopes:** `team_chat:read:file`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.file.get(file_id="LDG2jzoOS2aV4wkyLMaryg")
```

---

### List pending invitations
> Generates a list of a user's pending invitations. 

**Scopes:** `chat_channel:read`,`chat_channel:write`

**Granular Scopes:** `team_chat:read:list_invitations`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.invitiation.list(
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42", page_size=10
)
```

---

### List pending approvals
> Generates a list of a user's pending approvals to join a channel. 

**Scopes:** `chat_channel:read`,`chat_channel:write`

**Granular Scopes:** `team_chat:read:list_approvals`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.invitiation.approval.list(
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
)
```

---

### List admin pending external invitation approvals
> Retrieves a list of pending external invitations. (Account level app only.) 

Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate through chat in private or public groups.

**Scopes:** `chat_channel:write:admin`,`chat_channel:read:admin`

**Granular Scopes:** `team_chat:read:list_invitations:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.invitiation.approval.admin.list(
    invitation_direction="sent",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
)
```

---

### Get the invite link for a channel
> Returns the invite link for a channel.

**Scopes:** `chat_channel:read`,`chat_channel:write`

**Granular Scopes:** `team_chat:read:invite_link`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.invitiation.get_invite_link(channel_id="825c9e31f1064c73b394c5e4557d3447")
```

---

### List legal hold matters
> Returns a list of legal hold matters.

**Scopes:** `chat_history_legal_hold:read:admin`,`chat_history_legal_hold:write:admin`

**Granular Scopes:** `team_chat:read:list_legal_hold_matters:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `RESOURCE-INTENSIVE`

```python
client.chat.legalhold.matter.list(
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42", page_size=30
)
```

---

### List legal hold files by given matter
> Returns a list files for given legal hold matter.

**Scopes:** `chat_history_legal_hold:read:admin`,`chat_history_legal_hold:write:admin`

**Granular Scopes:** `team_chat:read:list_legal_hold_matter_files:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.legalhold.matter.file.list(
    matter_id="28c92682\-f4fc\-47b0\-bceb\-14cb839e0279",
    identifier="first\.last@test\.com",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=5,
)
```

---

### Download legal hold files for given matter
> Downloads a zip file.

**Scopes:** `chat_history_legal_hold:read:admin`,`chat_history_legal_hold:write:admin`

**Granular Scopes:** `team_chat:read:legal_hold_matter_file:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.legalhold.matter.file.download(
    matter_id="28c92682\-f4fc\-47b0\-bceb\-14cb839e0279",
    file_key="Zmlyc3QubGFzdEBleGFtcGxlLmNvbS0xNjc5NTg5MjMwNzY4",
)
```

---

### List bookmarks
> Returns the bookmarks for a given channel, 1:1 conversation, or across all of the sessions 

**Scopes:** `chat_message:read`,`chat_message:write`

**Granular Scopes:** `team_chat:read:list_bookmarks`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.message.bookmark.list(
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
    to_channel="qrstuvwxyz67890",
    to_contact="CxabcD3ojfdbjfg",
)
```

---

### List scheduled messages
> Returns a list of scheduled messages.

**Scopes:** `chat_message:read`,`chat_message:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.message.schedule.list(
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
    to_channel="825c9e31f1064c73b394c5e4557d3447",
    to_contact="helo@example\.com",
)
```

---

### List reminders
> Returns a list reminders for a person or a chat channel.

**Scopes:** `chat_message:read`,`chat_message:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.reminder.list(
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
    to_channel="cd102f7602c6428db0a273e632eb020B",
    to_contact="test@example\.com",
)
```

---

### List shared spaces
> Returns a list shared spaces.

**Scopes:** `chat:write:admin`,`chat:read:admin`,`chat:write`,`chat:read`

**Granular Scopes:** `team_chat:read:list_shared_spaces`,`team_chat:read:list_shared_spaces:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.list(
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size="30",
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
)
```

---

### Get a shared space
> Returns information about a shared space.

**Scopes:** `chat:read:admin`,`chat:read`,`chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:read:shared_space`,`team_chat:read:shared_space:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.get(space_id="bb31fa470fdc410cb76527282aa380d4")
```

---

### List shared space channels
> Returns a list of channels for a shared space.

**Scopes:** `chat:write:admin`,`chat:read:admin`,`chat:write`,`chat:read`

**Granular Scopes:** `team_chat:read:list_shared_space_channels`,`team_chat:read:list_shared_space_channels:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.channel.list(
    space_id="bb31fa470fdc410cb76527282aa380d4",
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    page_size=30,
)
```

---

### List shared space members
> Returns a list of members in a shared space.

**Scopes:** `chat:write:admin`,`chat:read:admin`,`chat:write`,`chat:read`

**Granular Scopes:** `team_chat:read:list_shared_space_members`,`team_chat:read:list_shared_space_members:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.channel.member.list(
    space_id="bb31fa470fdc410cb76527282aa380d4",
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    page_size=30,
    role="all",
    status="all",
)
```

---

### List user's contacts
> Lists all the contacts of a Zoom user. Zoom categorizes contacts into **company contacts** and **external contacts**. You must specify the contact type in the `type` query parameter. If you do not specify, by default, the type is set as company contact. A user under an organization's Zoom account has internal users listed under **company contacts** in the Zoom Client. A Zoom user can also add another Zoom user as a [contact](https://support.zoom.us/hc/en-us/articles/115004055706-Managing-Contacts).

**Note:** This API only supports **user-managed** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app).


**Scopes:** `chat_contact:read`

**Granular Scopes:** `team_chat:read:list_contacts`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.me.contact.list(
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42", page_size=10, type="company"
)
```

---

### Get user's contact details
> Returns information on a specific contact of the Zoom user. A user under an organization's Zoom account has internal users listed under Company Contacts in the Zoom Client. A Zoom user can also add another Zoom user as a [contact](https://support.zoom.us/hc/en-us/articles/115004055706-Managing-Contacts). 
**Note:** This API only supports **user-managed** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app).


**Scopes:** `chat_contact:read`

**Granular Scopes:** `team_chat:read:contact`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.me.contact.get(
    identifier="jchill@example\.com", query_presence_status=True
)
```

---

### List user's channels
> Generates a list of user's chat channels. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate through chat in private or public groups.

**Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:read:list_user_channels`,`team_chat:read:list_user_channels:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.channel.list(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
)
```

---

### Get a channel
> Returns information about a specific channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate through chat in private or public groups.

**Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:read:user_channel`,`team_chat:read:user_channel:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.channel.get(
    user_id="v4iyWT1LTfy8QvPG4GTvdg", channel_id="825c9e31f1064c73b394c5e4557d3447"
)
```

---

### List channel administrators
> Lists all administrators of a channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.



**Scopes:** `chat_channel:read`,`chat_channel:read:admin`

**Granular Scopes:** `team_chat:read:list_administrators:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.user.channel.admin.list(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
)
```

---

### List channel members
> Lists all members of a channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.



**Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:read:list_members`,`team_chat:read:list_members:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.user.channel.member.list(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=20,
)
```

---

### List user's chat messages
> Returns a list of chat messages and shared files between a user and an individual contact, or a chat channel. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  

**Note:** For an [account-level OAuth app](https://developers.zoom.us/docs/integrations/create/), this API can only be used on behalf of a [user assigned to a role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) with the **Edit** permission for **Chat Messages**. 



**Scopes:** `chat_message:write:admin`,`chat_message:read`,`chat_message:write`,`chat_message:read:admin`

**Granular Scopes:** `team_chat:read:list_user_messages`,`team_chat:read:list_user_messages:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.message.list(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    date="2020\-03\-01",
    download_file_formats="audio/mp4",
    exclude_child_message=True,
    from_query="2020\-02\-10T21:39:50Z",
    include_deleted_and_edited_message=True,
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
    search_key="hello",
    search_type="message",
    to="2020\-02\-15T12:00:00Z",
    to_channel="qrstuvwxyz67890",
    to_contact="string",
)
```

---

### Get a message
> Returns a chat message previously sent to a contact or a channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

You must provide one of the following query parameters:  
 
* `to_contact` &mdash; The email address of the Zoom contact to whom you sent the message.
* `to_channel` &mdash; The ID of the Zoom channel where you sent the message.



**Scopes:** `chat_message:write:admin`,`chat_message:read`,`chat_message:write`,`chat_message:read:admin`

**Granular Scopes:** `team_chat:read:user_message`,`team_chat:read:user_message:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.message.get(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    download_file_formats="audio/mp4",
    to_channel="cd102f7602c6428db0a273e632eb020B",
    to_contact="5UhQMZkDQ1CuuKVl1N5JIw",
)
```

---

### Retrieve a thread
> Retrieves all messages under a thread. For user-level apps, pass the `me` value instead of the `userId` parameter.

**Scopes:** `chat_message:read`,`chat_message:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.message.get_thread(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    from_query="2020\-05\-01T19:13:02Z",
    limit=30,
    need_attachment=True,
    need_emoji=False,
    need_main_message=True,
    sort="desc",
    to="2020\-05\-11T19:13:02Z",
    to_channel="0e3f7d76798f4991b11f8e1715887768",
    to_contact="example@example\.com",
)
```

---

### List a user's chat sessions
> Retrieves a user's chat sessions. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter. 

**Note:** For an **account-level** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app), you can only use this API on behalf of a user who is assigned a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management#:~:text=Each%20user%20in%20a%20Zoom,owner%2C%20administrator%2C%20or%20member.&amp;text=Role%2Dbased%20access%20control%20enables,needs%20to%20view%20or%20edit.) that has the **View** or **Edit** permission for **Chat Messages**.


**Scopes:** `chat_message:read`,`chat_message:read:admin`

**Granular Scopes:** `team_chat:read:list_user_sessions`,`team_chat:read:list_user_sessions:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.session.list(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    from_query="2020\-02\-10T21:39:50Z",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=10,
    search_star=True,
    to="2020\-02\-15T12:00:00Z",
    type="1:1",
)
```

---

### Search company contacts
> A user under an organization's Zoom account has internal users listed under Company Contacts in the Zoom Client. Use this API to search users that are in the company contacts of a Zoom account. Using the `search_key` query parameter, provide either first name, last name or the email address of the user that you would like to search for. Optionally, set `query_presence_status` to `true` in order to include the presence status of a contact.   
   
 



**Scopes:** `contact:read:admin`,`contact:read`

**Granular Scopes:** `contact:read:list_contacts`,`contact:read:list_contacts:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.contact.search(
    search_key="jchill@example\.com",
    contact_types=1,
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=20,
    query_presence_status=True,
    user_status="active",
)
```

---

### List IM directory groups
> List [IM directory groups](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management).  
   
 


**Scopes:** `imgroup:read:admin`,`imgroup:write:admin`

**Granular Scopes:** `contact_group:read:list_groups:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.im.group.list()
```

---

### Retrieve an IM directory group
> Retrieve an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.  
   
 
Scopes: `imgroup:read:admin`  
 

 

**Scopes:** `imgroup:read:admin`,`imgroup:write:admin`

**Granular Scopes:** `contact_group:read:group:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

```python
client.im.group.get(group_id="SobVexyrQjqCkcxjpBWi6w")
```

---

### List IM directory group members
> List the members of an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management).  
   
 


**Scopes:** `imgroup:read:admin`,`imgroup:write:admin`

**Granular Scopes:** `contact_group:read:list_members:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.im.group.member.update(
    group_id="SobVexyrQjqCkcxjpBWi6w",
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    page_number=1,
    page_size=30,
)
```

---

### Get chat sessions reports
> Gets Zoom Chat session reports for a specified period of time. The monthly date range **must** be within the last six months.

**Prerequisites:** 
* A Pro or higher plan 
* Report chat permissions.

**Scopes:** `report_chat:read:admin`,`imchat:read:admin`

**Granular Scopes:** `report:read:list_chat_sessions:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.report.chat.session.list(
    from_query="2020\-03\-01",
    to="2020\-04\-01",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=30,
)
```

---

### Get chat messages reports
> Gets Zoom Chat message reports for a specified period of time. The monthly date range must be within the last six months.

**Prerequisites:** 
* A Pro or higher plan 
* Report chat permissions

**Scopes:** `report_chat:read:admin`,`imchat:read:admin`

**Granular Scopes:** `report:read:chat_session:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.report.chat.session.get(
    session_id="5fdca6877b790503c027339a091e794498c146b849a1443d0c38d9ecd93b254d",
    from_query="2020\-03\-01",
    to="2020\-04\-01",
    include_bot_message=True,
    include_fields="edited_messages",
    next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
    page_size=30,
)
```

---

### Perform operations on the message of channel
> Performs different operations, such as pin or unpin, on the message of channel.  

**Scopes:** `chat:write`

**Granular Scopes:** `team_chat:update:pin_message`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.channel.message.update(
    data={
        "method": "pin",
        "message_id": "8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
        "channel_id": "825c9e31f1064c73b394c5e4557d3447",
    }
)
```

---

### Perform operations on channels
> Performs different operations on channels. 
Operations include archive and unarchive. It supports batch operations.

**Scopes:** `chat_channel:write:admin`,`chat_channel:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.channel.event.update(
    data={"method": "archive", "channel_ids": ["825c9e31f1064c73b394c5e4557d3447"]}
)
```

---

### Update a channel
> Update the name, type, and settings of a specific channel you own or administer. 



**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:update:channel`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.update(
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    data={
        "name": "Developers Channel",
        "channel_settings": {
            "add_member_permissions": 2,
            "new_members_can_see_previous_messages_files": True,
            "posting_permissions": 3,
            "mention_all_permissions": 1,
            "designated_posting_members": [{"user_id": "alsjdflasjfasjfas"}],
        },
        "type": 1,
    },
)
```

---

### Update retention policy of a channel
> Updates the retention policy of a channel.  

**Note:** This API only supports account-level apps. The user calling this API must have a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **Edit** permission for the **Chat Channels** feature.

**Scopes:** `chat_channel:write:admin`

**Granular Scopes:** `team_chat:update:retention:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.retention.update(
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    data={
        "cloud_retention": {"enable_custom_retention": True, "retention_period": "30m"}
    },
)
```

---

### Accept or reject an invitation
> Accept or reject an invitation to join a channel.

**Scopes:** `chat_channel:write`

**Granular Scopes:** `team_chat:update:invitation`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.invitiation.respond(
    data={
        "channel_id": "825c9e31f1064c73b394c5e4557d3447",
        "response": "accept_invitation",
    }
)
```

---

### Approve or deny a channel joining request as channel owner.
> Approves or denies a channel joining request as channel owner.

**Scopes:** `chat_channel:write`

**Granular Scopes:** `team_chat:update:approval`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.invitiation.approval.respond(
    data={
        "channel_id": "825c9e31f1064c73b394c5e4557d3447",
        "invitee_identifier": "zQmgS2TMSpGUOQcXyAHsyA",
        "response": "approve_invitation",
    }
)
```

---

### Admin approve or deny pending external invitations
> Approves or denies pending external invitations. (Only administrators can perform this task.)

**Scopes:** `chat_channel:write:admin`

**Granular Scopes:** `team_chat:update:invitations:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.invitiation.approval.admin.respond(
    data={"response": "approve", "invitation_ids": ["e2SfBv5KSUuSYACwRqOG6Q"]}
)
```

---

### Generate or reset invite link for a channel
> Generates or resets an invite link for a channel.

**Scopes:** `chat_channel:write`

**Granular Scopes:** `team_chat:update:invite_link`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.invitiation.update_invite_link(
    channel_id="825c9e31f1064c73b394c5e4557d3447"
)
```

---

### Update legal hold matter
> Updates the name for a given legal hold matter.

**Scopes:** `chat_history_legal_hold:write:admin`

**Granular Scopes:** `team_chat:update:legal_hold_matter:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.legalhold.matter.update(
    matter_id="28c92682\-f4fc\-47b0\-bceb\-14cb839e0279",
    data={"matter_name": "NewTest17888"},
)
```

---

### Add or remove a bookmark
> Adds a bookmark to a message or removes the bookmark from a message.

**Scopes:** `chat_message:write`

**Granular Scopes:** `team_chat:update:bookmark`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.message.bookmark.update(
    message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    data={
        "action": "add_bookmark",
        "to_channel": "825c9e31f1064c73b394c5e4557d3447",
        "to_contact": "jchill@example\.com",
    },
)
```

---

### Update shared space settings
> Updates a shared space's settings. Shared space owner can update `space_name`, `space_description`, and `space_settings`. Space admins can only update `space_name` and `space_description` unless the admin is also the space owner. 

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:update:shared_space`,`team_chat:update:shared_space:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.update(
    space_id="asdjfdwyntuuq3yqpmoixdq",
    data={
        "space_name": "Dev Space",
        "space_desc": "A dev's space\.",
        "space_settings": {
            "allow_to_add_external_users": 0,
            "add_member_permissions": 1,
            "create_channels_permission": 1,
        },
    },
)
```

---

### Move shared space channels
> Moves one or more channels in or out of a shared space. 


**Scopes:** `chat:write`

**Granular Scopes:** `team_chat:update:shared_space_channels`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.channel.move(
    space_id="8609fdea87b44e2f8e0f21ef3906046c",
    data={
        "channel_ids": ["8609fdea87b44e2f8e08609fdea87b44e2f8e0"],
        "move_direction": "move_into",
    },
)
```

---

### Transfer shared space ownership
> Transfers shared space ownership to a member or administrator.

 **Note:** This API supports account-level apps. The user calling this API must have a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **Edit** permission for the **Chat Channels** feature.

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:update:shared_space_owner`,`team_chat:update:shared_space_owner:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.transfer_owner(
    space_id="8609fdea87b44e2f8e0", identifier="zqmgs2tmspguoqcxyahsya"
)
```

---

### Update a channel
> Updates the name, type, and settings of a specific channel that the user owns or administers. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

Zoom chat channels allow users to communicate through chat in private or public channels.

**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:update:user_channel`,`team_chat:update:user_channel:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.channel.update(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    data={
        "name": "Developers Chat",
        "channel_settings": {
            "add_member_permissions": 2,
            "new_members_can_see_previous_messages_files": True,
            "posting_permissions": 3,
            "mention_all_permissions": 1,
            "designated_posting_members": [{"user_id": "alsjdflasjfasjfas"}],
        },
        "type": 1,
    },
)
```

---

### Star or unstar a channel or contact user
> Stars or unstars a contact or channel user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.



**Scopes:** `chat_event:write`,`chat_event:write:admin`

**Granular Scopes:** `team_chat:update:chat_control`,`team_chat:update:chat_control:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.event.update_star(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    data={
        "method": "star",
        "params": {
            "target_id": "825c9e31f1064c73b394c5e4557d3447",
            "target_type": "channel",
        },
    },
)
```

---

### React to a chat message
> Adds or removes an emoji to a chat message.

For an **account-level** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app), this API can only be used on behalf of a user who is assigned with a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management#:~:text=Each%20user%20in%20a%20Zoom,owner%2C%20administrator%2C%20or%20member.&amp;text=Role%2Dbased%20access%20control%20enables,needs%20to%20view%20or%20edit.) that has the **Edit** permission for **Chat Messages**.



**Scopes:** `chat_message:write`,`chat_message:write:admin`

**Granular Scopes:** `team_chat:update:message_emoji`,`team_chat:update:message_emoji:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.user.message.react(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    data={
        "action": "remove",
        "emoji": "U\+1F600",
        "to_channel": "825c9e31f1064c73b394c5e4557d3447",
        "to_contact": "jchill@example\.com",
    },
)
```

---

### Mark message read or unread
> Marks a chat message as read or unread. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter. 

**Note:** 

For an [account-level OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app), this API can only be used on behalf of a [user assigned to a role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) with the &quot;**Edit**&quot; permission for **Chat Messages**. 



**Scopes:** `chat_message:write`,`chat_message:write:admin`

**Granular Scopes:** `team_chat:update:message_status`,`team_chat:update:message_status:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.user.message.mark_status(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    data={
        "action": "read",
        "timestamp": 1581370790388,
        "to_channel": "825c9e31f1064c73b394c5e4557d3447",
        "to_contact": "jchill@example\.com",
    },
)
```

---

### Update an IM directory group
> Update an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.  
   
 


**Scopes:** `imgroup:write:admin`

**Granular Scopes:** `contact_group:update:group:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

```python
client.im.group.update(
    group_id="SobVexyrQjqCkcxjpBWi6w",
    data={
        "name": "Developers",
        "search_by_account": True,
        "search_by_domain": True,
        "search_by_ma_account": True,
        "type": "normal",
    },
)
```

---

### Search user's or account's channels
> Searches user's or account's chat channels.

**Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:write:search_channels`,`team_chat:write:search_channels:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `RESOURCE-INTENSIVE`

```python
client.chat.channel.search(
    data={
        "user_id": "v4iyWT1LTfy8QvPG4GTvdg",
        "page_size": 12,
        "next_page_token": "R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
        "needle": {"search_type": "by_channel_name", "keywords": ["spring"]},
        "haystack": "user_joined",
    }
)
```

---

### Invite channel members
> Invites members that are in a user's contact list to a channel. A [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) can have one or multiple members. The maximum number of members that can be added at once with this API is 5. 



**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:write:members`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.channel.member.invite(
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    data={"members": [{"email": "user@zoom\.us"}]},
)
```

---

### Invite channel members (Groups)
> Add members and groups to a channel.

**Scopes:** `chat_channel:write:admin`

**Granular Scopes:** `team_chat:write:groups:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.member.group.invite(
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    data={"groups": [{"group_id": "03dydv46RWKsMzUOdFGdeA"}]},
)
```

---

### Join a channel
> Joins a channel that is open for anyone in the same organization to join. A [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) can have one or more members. You cannot use this API to join private channels that only allow invited members to be a part of them.

**Note:** This API only supports **user-managed** [OAuth-app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app).


**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:write:member`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.channel.member.me.join(channel_id="825c9e31f1064c73b394c5e4557d3447")
```

---

### Add a custom emoji
> Add a custom emoji. 

 **Note:** 
* The base URL for this API's is `https://fileapi.zoom.us/v2`. 
* The rate limit of this API is 20 requests per second per API or 2000 requests per second per IP address. 
* The caller must support HTTP 30x redirects. 
* All files are sent as common files except `png`,`jpg`,`jpeg` and `gif` 
* The caller must retain the authorization header when redirected to a different hostname. 
 

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:write:custom_emoji`,`team_chat:write:custom_emoji:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.emoji.create(
    data={"name": "happy", "file": open("tests/fixtures/file.pdf", "rb")}
)
```

---

### Open a channel's invite link
> Opens a channel's invite link.

**Scopes:** `chat_channel:write`

**Granular Scopes:** `team_chat:write:open_invite_link`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.invitiation.join(
    data={
        "invite_link": "https://example\.com/invite/123e4567\-e89b\-12d3\-a456\-426614174000"
    }
)
```

---

### Add a legal hold matter
> Adds a new legal hold matter.

**Scopes:** `chat_history_legal_hold:write:admin`

**Granular Scopes:** `team_chat:write:legal_hold_matter:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `RESOURCE-INTENSIVE`

```python
client.chat.legalhold.matter.create(
    data={
        "start_date": "2024\-04\-01",
        "end_date": "2024\-04\-30",
        "matter_name": "Test17888",
        "identifiers": ["first\.last@test\.com"],
    }
)
```

---

### Create a reminder message
> Creates a reminder for a person or a chat channel. 

You must provide one of the following query parameters:
`to_contact` — The email address of the Zoom contact to whom you want to set the reminder.
`to_channel` — The ID of the Zoom channel where you set the reminder.

**Scopes:** `chat_message:write`,`chat_message:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

```python
client.chat.message.reminder.create(
    message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    data={
        "to_contact": "test@example\.com",
        "to_channel": "cd102f7602c6428db0a273e632eb020B",
        "remind_time": "2024\-02\-10T21:39:50Z",
        "delay_seconds": 1800,
        "reminder_note": "Reminder Note",
    },
)
```

---

### Migrate channel members
> Adds a maximum of 20 members to a migrated chat channel.

**Note**: The use of this endpoint is **locked**.  We make it available upon request on a case by case basis. To unlock this endpoint, contact [Zoom Support](https://support.zoom.com/hc/en/contact?id=contact_us). 

**Scopes:** `chat_migration:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.migration.channel.member.migrate(
    channel_id="649ad5f12f804cfea7dd7b1c1bb4c337",
    data={"members": [{"identifier": "qwwHGx5jSU2E1X46SLfGoA", "role": "admin"}]},
)
```

---

### Migrate chat message reactions
> Adds emoji reactions to a migrated chat message.

**Note**: The use of this endpoint is **locked**.  We make it available upon request on a case by case basis. To unlock this endpoint, contact [Zoom Support](https://support.zoom.com/hc/en/contact?id=contact_us). 

**Scopes:** `chat_migration:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.migration.migrate_reactions(
    data={
        "reactions": [
            {
                "message_id": "1679113305154",
                "message_timestamp": 1679113305154,
                "to_channel": "825c9e31f1064c73b394c5e4557d3447",
                "to_contact": "jchill@example\.com",
                "emojis": [
                    {
                        "emoji": "\+U1F400",
                        "user_identifier": ["649ad5f12f804cfea7dd7b1c1bb4c337"],
                    }
                ],
            }
        ]
    }
)
```

---

### Migrate chat messages
> Adds a maximum of 20 messages to migrated 1:1 conversations or channels.

**Note**: The use of this endpoint is **locked**.  We make it available upon request on a case by case basis. To unlock this endpoint, contact [Zoom Support](https://support.zoom.com/hc/en/contact?id=contact_us). 

**Scopes:** `chat_migration:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.migration.migrate_messages(
    data={
        "messages": [
            {
                "message_timestamp": 1679589230768,
                "sender": "649ad5f12f804cfea7dd7b1c1bb4c337",
                "to_channel": "825c9e31f1064c73b394c5e4557d3447",
                "to_contact": "jchill@example\.com",
                "message": "Hello",
                "file_ids": ["M87v\-bbmRGKCtl8nGNggvA"],
                "reply_main_message_id": "27ED2949\-6457\-417C\-83EA\-72515DAF00BD",
                "reply_main_message_timestamp": 1679589230768,
            }
        ]
    }
)
```

---

### Migrate a chat channel
> Migrates a chat channel.

**Note**: The use of this endpoint is **locked**.  We make it available upon request on a case by case basis. To unlock this endpoint, contact [Zoom Support](https://support.zoom.com/hc/en/contact?id=contact_us). 

**Scopes:** `chat_migration:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.migration.user.channel.migrate(
    identifier="649ad5f12f804cfea7dd7b1c1bb4c337",
    data={
        "members": [{"identifier": "xyzHGx5jSU2E1X46SLfBbq", "role": "admin"}],
        "type": 2,
        "name": "Developers",
        "created_time": "2023\-02\-13T15:23:14\.541Z",
    },
)
```

---

### Migrate 1:1 conversation or channel operations
> Performs operations on migrated 1:1 conversations or channels. For now, the only supported operation is to star 1:1 conversations or channels.

**Note**: By default, the use of this endpoint is **locked**. We make it available upon request on a case by case basis. To unlock this endpoint, contact [Zoom Support](https://support.zoom.com/hc/en/contact?id=contact_us). 

**Scopes:** `chat_migration:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.migration.user.event.migrate(
    identifier="649ad5f12f804cfea7dd7b1c1bb4c337",
    data={
        "method": "star",
        "params": [
            {"target_id": "825c9e31f1064c73b394c5e4557d3447", "target_type": "channel"}
        ],
    },
)
```

---

### Create a shared space
> Creates a shared space.

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:write:shared_space`,`team_chat:write:shared_space:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `RESOURCE-INTENSIVE`

```python
client.chat.space.create(
    data={
        "space_name": "Developer Group",
        "space_desc": "Developer discussion group\.",
        "space_members": [{"identifier": "1vRFhZt_2gipkB\-SFKkOpnkh", "role": "admin"}],
        "space_settings": {
            "allow_to_add_external_users": 0,
            "add_member_permissions": 1,
            "create_channels_permission": 1,
        },
    }
)
```

---

### Promote shared space members to administrators
> Promotes shared space members to administrators. 

**Note:** This API supports account-level apps. The user calling this API must have a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **Edit** permission for the **Chat Channels** feature.

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:write:shared_space_administrators`,`team_chat:write:shared_space_administrators:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.admin.promote(
    space_id="8609fdea87b44e2f8e0",
    data={"members": [{"identifier": "1vRFhZt_2gipkB\-SFKkOpnkh"}]},
)
```

---

### Add members to a shared space
> Adds members to a shared space. 

**Note:** This API supports account-level apps. The user calling this API must have a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **Edit** permission for the **Chat Channels** feature.

**Scopes:** `chat:write`,`chat:write:admin`

**Granular Scopes:** `team_chat:write:shared_space_members`,`team_chat:write:shared_space_members:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.space.channel.member.create(
    space_id="8609fdea87b44e2f8e0",
    data={"members": [{"identifier": "1vRFhZt_2gipkB\-SFKkOpnkh"}]},
)
```

---

### Create a channel
> Creates a channel for a user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter. Zoom chat channels allow users to communicate through chat in private or public groups.

**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:write:user_channel`,`team_chat:write:user_channel:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.channel.create(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    data={
        "channel_settings": {
            "add_member_permissions": 2,
            "new_members_can_see_previous_messages_files": True,
            "posting_permissions": 3,
            "mention_all_permissions": 1,
        },
        "members": [{"email": "jchill@example\.com"}],
        "name": "Developers",
        "type": 2,
    },
)
```

---

### Promote channel members to administrators
> Promote members to administrator role in a channel.  

For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.



**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:write:administrator:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.channel.admin.promote(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    data={"admins": [{"email": "jchill@example\.com"}]},
)
```

---

### Invite channel members
> Invites members that are in a user's contact list to a channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.



**Scopes:** `chat_channel:write`,`chat_channel:write:admin`

**Granular Scopes:** `team_chat:write:members`,`team_chat:write:members:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.chat.user.channel.member.invite(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    channel_id="825c9e31f1064c73b394c5e4557d3447",
    data={"members": [{"email": "jchill@example\.com"}]},
)
```

---

### Upload a chat file
> Uploads a file to chat. 

 **Note:** 
* The base URL for this API's is `https://file.zoom.us/v2/`. 
* The rate limit of this API is 20 requests per second per API or 2000 requests per second per IP address. 
* The caller must support HTTP 30x redirects. 
* All files are sent as common files except `png`,`jpg`,`jpeg` and `gif` 
* Zoom Cloud Storage will store the files sent through this API. If you do not use Zoom Cloud Storage, Zoom Cloud will temporarily store these files for 7 days. 
* The caller must retain the authorization header when redirected to a different hostname. 

 For an **account-level** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app), this API can only be used on behalf of a user who is assigned with a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management#:~:text=Each%20user%20in%20a%20Zoom,owner%2C%20administrator%2C%20or%20member.&amp;text=Role%2Dbased%20access%20control%20enables,needs%20to%20view%20or%20edit.) that has the **Edit** permission for **Chat Messages**. 

 

**Scopes:** `chat_message:write`,`chat_message:write:admin`

**Granular Scopes:** `team_chat:write:files`,`team_chat:write:files:admin`

```python
client.chat.user.file.upload(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    data={"file": open("tests/fixtures/file.pdf", "rb")},
)
```

---

### Send a chat message
> Sends chat messages to a user in your contact list or to a [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) of which you are a member.  
For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

- To send a message to a contact, provide the contact's email address in the `to_contact` field.  
- To send a message to a channel, provide the channel's ID in the `to_channel` parameter.



**Scopes:** `chat_message:write`,`chat_message:write:admin`

**Granular Scopes:** `team_chat:write:user_message`,`team_chat:write:user_message:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.message.send(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    data={
        "at_items": [
            {
                "at_contact": "jchill@example\.com",
                "at_type": 2,
                "end_position": 8,
                "start_position": 0,
            }
        ],
        "rich_text": [
            {
                "start_position": 0,
                "end_position": 1,
                "format_type": "Paragraph",
                "format_attr": "h1",
            }
        ],
        "message": "Hello",
        "file_ids": ["M87v\-bbmRGKCtl8nGNggvA"],
        "reply_main_message_id": "\{27ED2949\-6457\-417C\-83EA\-72515DAF00BD\}",
        "to_channel": "825c9e31f1064c73b394c5e4557d3447",
        "to_contact": "jchill@example\.com",
        "interactive_cards": [
            {
                "card_json": '\{   "content": \{     "settings": \{       "default_sidebar_color": "\#0E72ED",       "is_split_sidebar": false     \}   \} \}'
            }
        ],
        "scheduled_time": "2020\-02\-10T21:39:50Z",
    },
)
```

---

### Send a chat file
> Sends a file on Zoom to either an individual user in your contact list or a [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) of which you are a member. 

 **Note:** 
* The base URL for this API is `https://file.zoom.us/v2/`. 
* The rate limit of this API is 20 requests per second per API or 2000 requests per second per IP address. 
* The caller must support HTTP 30x redirects. 
* All files are sent as common files except `png`,`jpg`,`jpeg` and `gif` 
* Zoom Cloud Storage will store the files sent through this API. If you do not use Zoom Cloud Storage, Zoom Cloud will temporarily store these files for 7 days. 
* The caller must retain the authorization header when redirected to a different hostname. 

For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter. 

 For an [account-level OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app), this API can only be used on behalf of a user who is assigned with a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management) that has the **Edit** permission for **Chat Messages**. 

 

**Scopes:** `chat_message:write`,`chat_message:write:admin`

**Granular Scopes:** `team_chat:write:message_files`,`team_chat:write:message_files:admin`

```python
client.chat.user.file.send(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    data={
        "files": [open("tests/fixtures/file.pdf", "rb")],
        "reply_main_message_id": "8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
        "to_channel": "825c9e31f1064c73b394c5e4557d3447",
        "to_contact": "za7AvP7o9AxypYwpaKYsOJ2K3VwXBZn4JtxgPGk8Lf7_1w",
    },
)
```

---

### Create an IM directory group
> Create an IM directory group under your account.  
   
 


**Scopes:** `imgroup:write:admin`

**Granular Scopes:** `contact_group:write:group:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

```python
client.im.group.create(
    data={
        "name": "Developers",
        "search_by_account": True,
        "search_by_domain": True,
        "search_by_ma_account": True,
        "type": "normal",
    }
)
```

---

### Add IM directory group members
> Add members to an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under an account.  
   
 


**Scopes:** `imgroup:write:admin`

**Granular Scopes:** `contact_group:write:member:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

```python
client.im.group.member.create(
    group_id="SobVexyrQjqCkcxjpBWi6w",
    data={
        "members": [{"email": "jchill@example\.com", "id": "v4iyWT1LTfy8QvPG4GTvdg"}]
    },
)
```

---

### Send IM messages
> Sends the chat message to a user.

**Note:** This API only supports OAuth 2.0.


**Scopes:** `imchat:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.im.user.me.chat.message.send(
    chat_user="jchill@example\.com", data={"message": "hello, world!"}
)
```

---

### Update a message
> Edits a chat message that you previously sent to either a contact or a channel in Zoom. 

It provides the ID of the message as the value of the `messageId` parameter. You can get the ID from the [List User's Chat Messages](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getChatMessages) API. Additionally, as a query parameter, you must provide either the contact's **email address** of the contact or the **Channel ID** of the channel where the message was sent.

For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

**Note:** For an **account-level** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app), you can only use this API on behalf of a user who is assigned with a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Using-role-management#:~:text=Each%20user%20in%20a%20Zoom,owner%2C%20administrator%2C%20or%20member.&amp;text=Role%2Dbased%20access%20control%20enables,needs%20to%20view%20or%20edit.) that has the **Edit** permission for **Chat Messages**.



**Scopes:** `chat_message:write`,`chat_message:write:admin`

**Granular Scopes:** `team_chat:update:user_message`,`team_chat:update:user_message:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

```python
client.chat.user.message.update(
    user_id="v4iyWT1LTfy8QvPG4GTvdg",
    message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
    data={
        "message": "Hello there\.",
        "to_channel": "825c9e31f1064c73b394c5e4557d3447",
        "to_contact": "jchill@example\.com",
        "file_ids": ["M87v\-bbmRGKCtl8nGNggvA"],
        "interactive_cards": [{"card_id": "xBvggqyjQUal6TecwMlYwQ"}],
    },
)
```


