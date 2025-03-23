// The Swift Programming Language
// https://docs.swift.org/swift-book

func pp1(_ name: String, _ val: Any) {
    let valType = type(of: val)
    let pVal = val is String ? "\"\(val)\"" : val

    print("type: \(valType), \(name)=\(pVal)")
}

print("Hello, world!")

pp1("x", "hello, world!")

var x1:String?=nil
pp1("x1", x1)

x1 = "hi"
pp1("x1", x1)
