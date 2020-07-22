package main

import "fmt"

func main() {
	// three urns labeled X, Y, Z
	// urn X = 4 red balls, 3 black balls
	// urn Y = 5 red balls, 4 black balls
	// urn Z = 4 red balls, 4 black balls
	// -1 from each urn, probability that balls drawn are 2 red and 1 black
	xR := 4
	xB := 3
	xT := xR + xB
	Pxr := float32(xR) / float32(xT)
	Pxb := float32(xB) / float32(xT)

	yR := 5
	yB := 3
	yT := yR + yB
	Pyr := float32(yR) / float32(yT)
	Pyb := float32(yB) / float32(yT)

	zR := 4
	zB := 4
	zT := zR + zB
	Pzr := float32(zR) / float32(zT)
	Pzb := float32(zB) / float32(zT)

	//Ptr := (float32(xR) * float32(yR) * float32(zR)) / (float32(xT) * float32(yT) * float32(zT))
	Ptr := Pxr * Pyr * Pzr
	Ptb := Pxb * Pyb * Pzb

	fPxr := fmt.Sprintf("P(X red) = %d / %d = %.5f", xR, xT, Pxr)
	fPxb := fmt.Sprintf("P(X black) = %d / %d = %.5f", xB, xT, Pxb)

	fPyr := fmt.Sprintf("P(Y red) = %d / %d = %.5f", yR, yT, Pyr)
	fPyb := fmt.Sprintf("P(Y black) = %d / %d = %.5f", yB, yT, Pyb)

	fPzr := fmt.Sprintf("P(Z red) = %d / %d = %.5f", zR, zT, Pzr)
	fPzb := fmt.Sprintf("P(Z black) = %d / %d = %.5f", zB, zT, Pzb)

	fPtr := fmt.Sprintf("P(Total red) = %d / %d = %.5f", (xR * yR * zR), (xT * yT * zT), Ptr)
	fPtb := fmt.Sprintf("P(Total black) = %d / %d = %.5f", (xB * yB * zB), (xT * yT * zT), Ptb)

	fmt.Println(fPxr)
	fmt.Println(fPxb)
	fmt.Println(fPyr)
	fmt.Println(fPyb)
	fmt.Println(fPzr)
	fmt.Println(fPzb)
	fmt.Println(fPtr)
	fmt.Println(fPtb)
	fmt.Println(Ptr, " x 2 = ", Ptr*2)
	fmt.Println(" + ", Ptb, " = ", (Ptr*2)+Ptb)
}
