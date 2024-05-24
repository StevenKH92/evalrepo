import os
import asyncio
from groq import AsyncGroq

client = AsyncGroq(
    # This is the default and can be omitted
    api_key=os.environ.get("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"),
)


async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of low latency LLMs",
            }
        ],
        model="llama3-8b-8192",
    )
    print(chat_completion.choices[0].message.content)


asyncio.run(main())
