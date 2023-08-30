import uvicorn


def main():
    uvicorn.run(
        "app.application:app",
        # TODO const.uvicorn에 있는 애들로 변경
        port=8000,
        reload=True,
    )

if __name__ == "__main__":
    main()