// The Swift Programming Language
// https://docs.swift.org/swift-book
//
// Swift Argument Parser
// https://swiftpackageindex.com/apple/swift-argument-parser/documentation

import ArgumentParser
import Foundation

@main
struct Demo01: ParsableCommand {
    mutating func run() throws {
        print("Hello, world!")

        print()

        demoBasics()

        print()

        demoBasicOperators()

        print()

        demoStringsAndCharacters()

        print()

        demoCollectionTypes()
    }
}

// _ : ommit argument label
func pp1<T>(_ val: T, _ name: String = "v") {
    if let coll = val as? any Collection {
        let valStr: String
        if let s = coll as? any StringProtocol {
            valStr = "'\(s)'"
        } else {
            valStr = "\(coll)"
        }
        print("type: \(type(of: val)), count: (\(coll.count)), \(name)=\(valStr)")
    } else {
        print("type: \(type(of: val)), \(name)=\(val)")
    }
}

// ... : variadic parameters
func pp3(_ variables: (Any, String)...) {
    for (val, name) in variables {
        pp1(val, name)
    }
}

func demoBasics() {
    print(
        """

        ============
        demoBasics()
        ============

        """)
    // variables must be initialized before using
    // no type annotation
    // type inference
    var x1 = 8
    var x2 = 8.8
    var x3 = "var variable without type annotation"
    pp1(x1, "x1")
    pp1(x2, "x2")
    pp1(x3, "x3")
    print("x1=\(x1), x2=\(x2), x3=\(x3)")
    x1 = 9
    x2 = 10
    x3 = "empty it"
    print("x1=\(x1), x2=\(x2), x3=\(x3)")

    print()

    // with type annotation
    // it's rare to write type annotations in practice.
    var n1: Int = 0
    var n2: Float = 0.1
    var n3: Double = 0.2
    var n4: Bool = false
    var n5: String = ""
    var n6: [Int] = []
    var n7: [String: Int] = [:]
    print(
        """
        n1=\(n1), n2=\(n2), n3=\(n3),
        n4=\(n4), n5=\(n5), n6=\(n6),
        n7=\(n7)
        """)
    n1 = 2
    n2 = 2.2
    n3 = 2.8
    n4 = true
    n5 = "hello from var variable"
    n6 = [45, 43, 42, 41]
    n7 = ["country": 9, "city": 8]
    print(
        """
        n1=\(n1), n2=\(n2), n3=\(n3),
        n4=\(n4), n5=\(n5), n6=\(n6),
        n7=\(n7)
        """)

    print()

    // constants
    let m1 = 1
    let m2 = 1.1
    let m3 = true
    let m4 = "hello from constant variable"
    let m5 = [1, 2, 3, 4, 5.5]
    let m6 = ["name": "foot", "age": "20"]
    print(
        """
        m1=\(m1), m2=\(m2), m3=\(m3),
        m4=\(m4), m5=\(m5), m6=\(m6)
        """)

    print()

    // single-line comment
    // another one

    /*
     multiline comments
     string interpolation to wrap variable name in parenthesis and escape it with a back-slash
     */
    let name = "Swift"
    let version = 6.0
    print("My name is \(name), and my version is \(version)")
}

func demoBasicOperators() {
    print(
        """

        ====================
        demoBasicOperators()
        ====================

        """)
    // assignment operator
    let a = 10
    var b = 5
    print("a=\(a), b=\(b)")
    b = a
    print("a=\(a), b=\(b)")

    print()

    let (x, y) = (4, 3)
    print("x=\(x), y=\(y)")

    print()

    // Arithmetic operators
    let a1 = 4 + 3  // addition operator
    let a2 = 4 - 3  // substraction operator
    let a3 = 4 * 3  // multiplication operator
    let a4 = 4 / 3  // division operator
    let a5 = 4 % 3  // remainder operator
    let a6 = 4.0 / 3.0
    let a7 = "hello " + " strings!"
    print(
        "4 + 3 = \(a1), 4 - 3 = \(a2), 4 * 3 = \(a3), 4 / 3 = \(a4), 4 % 3 = \(a5), 4.0 / 3.0 = \(a6)",
        terminator: "")
    print(" \"hello\" + \" strings!\" = \(a7)")

    print()

    // Compound assignment operators
    var c1 = 1
    print("c1=\(c1)", terminator: ", ")
    c1 += 11
    print("c1 += 11, c1 = \(c1)", terminator: ", ")
    c1 -= 1
    print("c1 -= 1, c1 = \(c1)", terminator: ", ")
    c1 *= 6
    print("c1 *= 6, c1 = \(c1)", terminator: ", ")
    c1 /= 2
    print("c1 /= 2, c1 = \(c1)", terminator: ", ")

    print()

    // Unary minus operator
    let b1 = 10
    let b2 = -b1
    print("b1=\(b1), b2=\(b2)")

    print()

    // Comparison operators
    print("(1 == 1) = \(1 == 1)", terminator: ", ")  // equal to
    print("(1 != 1) = \(1 != 1)", terminator: ", ")  // not equal to
    print("(1 > ) = \(1 > 1)", terminator: ", ")  // greater than
    print("(1 >= 1) = \(1 >= 1)", terminator: ", ")  // greater than or equal to
    print("(1 < 1) = \(1 < 1)", terminator: ", ")  // less than
    print("(1 <= 1) = \(1 <= 1)")  // less than or equal to

    print()

    // compare tuples
    print("((1, \"apple\") < (2, \"banana\")) = \((1, "apple") < (2, "banana"))", terminator: ", ")
    print("((1, \"apple\") > (1, \"banana\")) = \((1, "apple") > (1, "banana"))", terminator: ", ")
    print("((1, \"apple\") == (1, \"banana\")) = \((1, "apple") == (1, "banana"))", terminator: ", ")

    print()
    print()

    // Ternary conditional operator
    let d1 = 5
    let d2 = 3
    let d3 = d1 > d2 ? d1 : d2
    print("d1=\(d1), d2=\(d2), (d1 > d2 ? d1 : d2) = \(d3)")

    print()

    // Nil-Coalescing operator
    let defaultColor = "red"
    var userColor: String?
    print("defaultColor=\(defaultColor), (userColor ?? \"nil\") = \(userColor ?? "nil")")

    // if userColor is nil(null or none), then use `defaultColor`
    var colorToUse = userColor ?? defaultColor
    print("defaultColor=\(defaultColor), colorToUse=\(colorToUse)")

    userColor = "blue"
    colorToUse = userColor ?? defaultColor
    print("defaultColor=\(defaultColor), colorToUse=\(colorToUse)")

    print()

    // Range operators
    // closed range operator
    let e1 = 1...5
    print(e1.contains(2), e1.contains(5), e1.contains(6))
    print("")
    for i in e1 {
        print(i, terminator: ", ")
    }
    print()
    // half-open range
    let e2 = 1..<5
    for i in e2 {
        print(i, terminator: ", ")
    }
    print()
    let names = ["Bob", "Peter", "Tom", "Cindy"]
    for i in 0..<names.count {
        print(names[i], terminator: " .. ")
    }
    print()
    let arr1 = [0, 1, 2, 3, 4, 5, 6]
    print(arr1)
    // one-side range
    print(arr1[...2], arr1[3...])
    print(arr1[..<2], arr1[2...])

    print()

    // logical operators
    let bt1 = true
    let bt2 = false
    print(bt1 && bt2, terminator: ", ")  // `&&` logical AND operator
    print(bt1 || bt2, terminator: ", ")  // `||` logcial OR operator
    print(!bt1, !bt2)  // `!` logical NOT operator

    print()

    // combining logical operators
    // `a && b && c || d || e`
}

func demoStringsAndCharacters() {
    print(
        """

        ==========================
        demoStringsAndCharacters()
        ==========================

        """)
    // String literals
    let singleLineString = "These are the same."
    // Multiline string literals
    let multiineString = """
        These are the same.
        """
    print(
        "(singleLineString == multilineString) = \(singleLineString == multiineString)"
    )

    print()

    let ms1 = """
        Hello, this multiline string is
        in two lines
        """

    let ms2 = """
        Hello, this multiline string is \
        in single lines
        """
    print(ms1)

    print()

    print(ms2)

    print()

    // Special characters
    // `\0` , `\\`, `\t`, `\n`, `\r`, `\"` , `\'`
    let ms3 = """
        This multiline string contains null character(\0), backslack(\\), horizontal tab(\t), line feed(\n), \
        carriage return(\r), double quotation mark(\" or "), single quotation mark(\' or '), \
        three double quotation marks(\""")
        """
    print(ms3)

    print()

    // extende string delimiters
    // just print the literal string, no escaping.
    let ms4 = #"""
        This multiline string contains null character(\0), backslack(\\), horizontal tab(\t), line feed(\n), \
        carriage return(\r), double quotation mark(\" or "), single quotation mark(\' or '), \
        three double quotation marks(\""")
        """#
    print(ms4)

    print()

    let ss1 =
        "unicode characters: dollar sign(\u{24}), black heart(\u{2665}), sparking heart(\u{1F496})"
    let ss2 =
        #"unicode characters: dollar sign(\u{24}), black heart(\u{2665}), sparking heart(\u{1F496})"#
    print(ss1)
    print(ss2)

    print()

    let emptyStr = ""
    if emptyStr.isEmpty {
        print("var \"emptyStr\" is an empty string")
    }
    let helloStr = "hello there"
    print("count: \(helloStr.count)", terminator: ", ")
    pp1(helloStr)

    print()

    // character
    for c in "Dog!🐶" {
        pp1(c)
    }

    print()

    let c1: Character = "!"
    let ccs: [Character] = ["a", "b", "\"", "1"]
    let s1 = String(ccs)
    pp1(c1)
    pp1(ccs)
    pp1(s1)

    print()

    // Concatenate strings
    let str1 = "hello"
    let str2 = " there"
    let str3 = str1 + str2
    pp1(str1)
    pp1(str2)
    pp1(str3)

    print()

    var v1 = "look"
    pp1(v1)
    pp1(str2)
    v1 += str2
    pp1(v1)

    v1.append(" a big cat!")
    pp1(v1)

    print()

    // string interpolation
    print("6 times 7 is \(6 * 7).")
    print(#"6 times 7 is \(6 * 7)."#)
    print(#"6 times 7 is \#(6 * 7)."#)

    print()

    // unicode
    let eAcute: Character = "\u{E9}"                         // é
    let combinedEAcute: Character = "\u{65}\u{301}"          // e followed by
    pp1(eAcute, "eAcute")
    pp1(combinedEAcute, "combinedEAcute")

    print()

    let eAcuteStr = "\u{E9}"                         // é
    let combinedEAcuteStr = "\u{65}\u{301}"          // e followed by
    pp1(eAcuteStr, "eAcuteStr")
    pp1(combinedEAcuteStr, "combinedEAcuteStr")
    print("(eAcuteStr == combinedEAcuteStr)=\(eAcuteStr == combinedEAcuteStr)")

    print()

    // Swift strings can’t be indexed by integer values
    let s9 = "hello, baby é ?"
    // get the startIndex, endIndex, and other index
    print("startIndex: \(s9.startIndex), after startIndex:\(s9.index(after:s9.startIndex))")
    print("endIndex: \(s9.endIndex), before endIndex:\(s9.index(before:s9.endIndex))")
    print("any index(from startIndex, offset by 4): \(s9.index(s9.startIndex, offsetBy: 4))")
    print()
    // interate all the indexes(indices)
    for index in s9.indices {
        print("index:\(index), value:'\(s9[index])'")
    }
    // interate all the characters
    for c1 in s9 {
        print("\(c1)", terminator: "_")
    }
    print()

    print()

    // insert
    var welcomeStr = "hello there"
    pp1(welcomeStr, "welcomeStr")
    // insert one character
    welcomeStr.insert("!", at: welcomeStr.endIndex)
    pp1(welcomeStr, "welcomeStr")
    // insert a string
    welcomeStr.insert(contentsOf: " How are you", at: welcomeStr.index(before: welcomeStr.endIndex))
    pp1(welcomeStr, "welcomeStr")

    print()

    // remove a character
    welcomeStr.remove(at: welcomeStr.index(before: welcomeStr.endIndex))
    pp1(welcomeStr, "welcomeStr")
    // remove a substring
    let rangeToRemove = welcomeStr.index(welcomeStr.endIndex, offsetBy: -12)..<welcomeStr.endIndex
    welcomeStr.removeSubrange(rangeToRemove)
    pp1(welcomeStr, "welcomeStr")

    print()

    // substring, an instance of `SubString`, not a string
    let spaceIndex = welcomeStr.firstIndex(of: " ") ?? welcomeStr.endIndex
    let firstSubStr = welcomeStr[..<spaceIndex]
    let secondSubStr = welcomeStr[welcomeStr.index(after: spaceIndex)...]
    pp1(firstSubStr, "firstSubStr")
    pp1(secondSubStr, "secondSubStr")

    print()

    // save substring to a `String`
    let firstStr = String(firstSubStr)
    let secondStr = String(secondSubStr)
    pp1(firstStr, "firstStr")
    pp1(secondStr, "secondStr")

    print()

    // compare strings
    // use `==` or `!=` to compare strings
    let sameStr1 = "same str!"
    let sameStr2 = "same str!"
    print("(sameStr1 == sameStr2)=\(sameStr1 == sameStr2)")
    print("(sameStr1 != sameStr2)=\(sameStr1 != sameStr2)")

    print()

    let romeoAndJuliet = [
        "Act 1 Scene 1: Verona, A public place",
        "Act 1 Scene 2: Capulet's mansion",
        "Act 1 Scene 3: A room in Capulet's mansion",
        "Act 1 Scene 4: A street outside Capulet's mansion",
        "Act 1 Scene 5: The Great Hall in Capulet's mansion",
        "Act 2 Scene 1: Outside Capulet's mansion",
        "Act 2 Scene 2: Capulet's orchard",
        "Act 2 Scene 3: Outside Friar Lawrence's cell",
        "Act 2 Scene 4: A street in Verona",
        "Act 2 Scene 5: Capulet's mansion",
        "Act 2 Scene 6: Friar Lawrence's cell",
    ]
    var act1SceneCount = 0
    for scene in romeoAndJuliet {
        if scene.hasPrefix("Act 1") {
            act1SceneCount += 1
        }
    }
    print("There are \(act1SceneCount) scenes in Act 1")

    var mansionCount = 0
    var cellCount = 0
    for scene in romeoAndJuliet {
        if scene.hasSuffix("mansion") {
            mansionCount += 1
        }
        if scene.hasSuffix("cell") {
            cellCount += 1
        }
    }
    print("\(mansionCount) mansion scenes, \(cellCount) cell scenes.")

    print()

    let dogString = "Dog‼🐶"
    pp1(dogString, "dogString")

    for codeUnit in dogString.utf8 {
        print("\(codeUnit)", terminator: "_")
    }
    print()
    for codeUnit in dogString.utf16 {
        print(codeUnit, terminator: "_")
    }
    print()
    for scalar in dogString.unicodeScalars {
        print("\(scalar)-\(scalar.value)", terminator: "_")
    }
    print()
    for (char, scalar) in zip(dogString, dogString.unicodeScalars) {
        print("\(char)_\(scalar)-\(scalar.value)", terminator: "_")
    }
    print()
}

func demoCollectionTypes() {
    // empty array
    let emptyStrs = [String]()
    let emptyInts: [Int] = []
    pp1(emptyInts, "emptyInts")
    pp1(emptyStrs, "emptyStrs")
    print("for `emptyInts` -> count: \(emptyInts.count), is empty: \(emptyInts.isEmpty)")

    print()

    // with default value
    var fiveInts = Array(repeating: 9, count: 5)
    let sixDoubles = Array(repeating: 0.0, count: 6)
    let sevenStrs = Array(repeating: "hi", count: 7)
    pp1(sixDoubles, "sixDoubles")
    pp1(sevenStrs, "sevenStrs")
    pp1(fiveInts, "fiveInts")
    // append a value
    fiveInts.append(10)
    pp1(fiveInts, "fiveInts")

    // array literal
    let threeInts = [99, 88, 111]
    let fourInts = [1, 2, 3, 5]
    var moreInts = threeInts + fourInts
    pp1(threeInts, "threeInts")
    pp1(fourInts, "fourInts")

    print()

    pp1(moreInts, "moreInts")
    // append one element
    moreInts.append(7)
    pp1(moreInts, "moreInts")
    // append another array
    moreInts += [11, 13]
    pp1(moreInts, "moreInts")

    print()

    // access by subscript syntax
    pp1(moreInts[0], "moreInts[0]")
    pp1(moreInts[1], "moreInts[1]")
    pp1(moreInts[2...6], "moreInts[2...6]")

    print()

    // set the value by subscript syntax
    moreInts[0] = 999
    pp1(moreInts[0], "moreInts[0]")
    moreInts[2...6] = [11, 22, 33, 55]
    pp1(moreInts, "moreInts")

    print()

    // insert a value
    moreInts.insert(321, at: 0)
    pp1(moreInts, "moreInts")

    // remove a value
    moreInts.remove(at: 1)
    pp1(moreInts, "moreInts")
    let lastVal = moreInts.removeLast()
    pp1(lastVal, "lastVal")
    pp1(moreInts, "moreInts")

    print()

    // iterate over an array
    for n in moreInts {
        pp1(n)
    }

    // iterate over an array with index and value
    for (index, v) in moreInts.enumerated() {
        print("\(index) : \(v)")
    }

    print()

    // Sets
    // empty set
    let emptyIntSet = Set<Int>()
    pp1(emptyIntSet, "emptyIntSet")
    print("count: \(emptyIntSet.count), is empty: \(emptyIntSet.isEmpty)")

    print()

    // create set with an array literal
    let twoStrSet: Set = ["hello", "hi"]
    pp1(twoStrSet, "twoStrSet")

    print()

    var moreStrSet: Set<String> = []
    pp1(moreStrSet, "moreStrSet")
    moreStrSet.insert("Tom")
    pp1(moreStrSet, "moreStrSet")
    moreStrSet.insert("Jerry")
    pp1(moreStrSet, "moreStrSet")
    moreStrSet.insert("Cat")
    pp1(moreStrSet, "moreStrSet")
    moreStrSet.insert("Mouse")
    pp1(moreStrSet, "moreStrSet")
    moreStrSet.remove("Mouse")
    pp1(moreStrSet, "moreStrSet")
    moreStrSet.remove("Mouse")
    pp1(moreStrSet, "moreStrSet")

    print()

    print("contains(\"Cat\"): \(moreStrSet.contains("Cat"))")

    print()
    // iterate over a set
    for s in moreStrSet {
        pp1(s)
    }

    print()

    // iterator over a sorted set
    for s in moreStrSet.sorted() {
        pp1(s)
    }

    print()

    // set operations
    let oddDigits: Set = [1, 3, 5, 7, 9]
    let evenDigits: Set = [0, 2, 4, 6, 8, 10]
    let primeNumbers: Set = [2, 3, 5, 7, 11]

    pp1(oddDigits, "oddDigits")
    pp1(evenDigits, "evenDigits")
    pp1(primeNumbers, "primeNumbers")

    print()

    pp1(oddDigits.union(evenDigits), "oddDigits | evenDigits")
    pp1(oddDigits.intersection(evenDigits), "oddDigits & evenDigits")
    pp1(oddDigits.subtracting(primeNumbers), "oddDigits - primeNumbers")
    pp1(oddDigits.symmetricDifference(primeNumbers), "oddDigits ^ primeNumbers")

    print()

    let moreOddDigits: Set = Set(Array(oddDigits) + [11, 13, 15])
    pp1(oddDigits == moreOddDigits, "(oddDigits == moreOddDigits)")
    pp1(oddDigits.isSubset(of: moreOddDigits), "(oddDigits is in moreOddDigits)")
    pp1(oddDigits.isStrictSubset(of: moreOddDigits), "(oddDigits is totally in moreOddDigits)")
    pp1(oddDigits.isSuperset(of: moreOddDigits), "(oddDigits contains moreOddDigits)")
    pp1(oddDigits.isDisjoint(with: moreOddDigits), "(oddDigits is disjoint with moreOddDigits)")

    print()

    // dictionaries
    var emptyDict: [Int: String] = [:]
    pp1(emptyDict, "emptyDict")
    print("count: \(emptyDict.count), is empty: \(emptyDict.isEmpty)")

    emptyDict[8] = "eighth"
    pp1(emptyDict, "emptyDict")

    print()

    // create dictionary with literal
    var airports = ["YYZ": "Toronto Pearson", "DUB": "Dublin"]
    pp1(airports, "airports")

    // update dictionary by key
    airports["PEK"] = "Beijing"
    pp1(airports, "airports")
    airports["PEK"] = "Beijing Captical"
    pp1(airports, "airports")
    let oldName = airports.updateValue("Dublin airport", forKey: "DUB")
    pp1(oldName, "oldName")
    pp1(airports, "airports")

    // remove a value
    airports["ABC"] = "Unknown"
    pp1(airports, "airports")
    airports.removeValue(forKey: "ABC")
    pp1(airports, "airports")

    print()

    // iterate over a dictionary
    for (k, v) in airports {
        print("\(k): \(v)")
    }
    print()
    // iterate over keys
    pp1(airports, "airports")
    pp1(airports.keys)
    pp1(airports.values)
    print()
    for k in airports.keys {
        pp1(k)
    }
    print()
    // iterate over values
    for v in airports.values {
        pp1(v)
    }
    print()

    print()

}
