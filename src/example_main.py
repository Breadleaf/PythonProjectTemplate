import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import util.TestSuite as TS
import util.Reference as REF


def strcmp(a: str, b: str) -> bool:
    print(f"Comparing '{a}' to '{b}'")
    return a == b


if __name__ == "__main__":
    data: str = "Hello, World!"
    ref: REF.Reference = REF.Reference(data)

    # Setup the Unit Test
    suite: TS.TestSuite = TS.TestSuite("Boilerplate Code Demo!")

    # You can add code that will execute at the very beginning of the test suite
    # NOTE: This is optional
    # NOTE: If you do use this, it MUST return True else the test suite will skip
    #       This can be used to conditionally skip the entire test suite
    suite.setSetup(
        lambda: ref.setData(
            ref.getData().replace("World", "Unit Test")
        ) or True
    )

    # You can add code that will execute before each individual test
    # NOTE: This is optional
    # NOTE: If you do use this, it MUST return True else specific test will skip
    #       This can be used to conditionally skip tests
    suite.setBefore(
        lambda: print(
            ref.getData()
        ) or True
    )

    # Add the tests to the suite
    # NOTE: There must be at least one test for the suite to run
    suite.addTest(
        "Test 1",
        lambda: strcmp(ref.getData(), data)
    )

    suite.addTest(
        "Test 2",
        lambda: strcmp(ref.getData(), "Hello, Unit Test!")
    )

    # Run the tests, and print the results in a summary
    suite.runTests()