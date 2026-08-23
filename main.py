import asyncio

from agent import get_agent


async def main():

    agent = await get_agent()

    response = await agent.ainvoke(
        {
            "messages": [
                (
                    "What is the cappital of France"
                )
            ]
        }
    )

    print("\nFinal response:")
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())