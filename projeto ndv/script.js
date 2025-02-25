const beforetext = document.querySelector("#before");
const aftertext = document.querySelector("#after");
const buttons = document.querySelectorAll("#buttons button");


class calculator {
    constructor(beforetext, aftertext){
        this.beforetext = beforetext
        this.aftertext = aftertext
        this.currentoperation = ""
    }


    addDigit(digit) {

        if(digit === "." && this.aftertext.innerText.includes(".")) {
            return;
        }

        this.currentoperation = digit
        this.updateScreen()
    }


    processOperation(operation) {
        
        if(this.aftertext.innerText === "" && operation !== "C") {
            if(this.beforetext.innerText !== "") {
                this.changeOperation(operation);
            }
            return;
        }


        let operationValue;
        const previous = +this.beforetext.innerText.split(" ")[0];
        const current = +this.aftertext.innerText;

        switch(operation) {
            case "+":
                operationValue = previous + current;
                this.updateScreen(operationValue,operation, current, previous);
                break;
            case "-":
                operationValue = previous - current;
                this.updateScreen(operationValue,operation, current, previous);
                break;
            case "x":
                operationValue = previous * current;
                this.updateScreen(operationValue,operation, current, previous);
                break;
            case "÷":
                operationValue = previous / current;
                this.updateScreen(operationValue,operation, current, previous);
                break;
            case "DEL":
                this.processDelOperator();
                break;
            case "CE":
                this.clearCurrentOperation();
                break;
            case "C":
                this.clearAllOperation();
                break;
            case "=":
                this.EqualOperation();
                break;

            default:
                return; 

        }

    }


    updateScreen(operationValue = null, operation = null, current = null, previous = null){
        if(operationValue === null) {
            this.aftertext.innerText += this.currentoperation; 
        }else {
             if(previous === 0) {
                operationValue = current
             }

             this.beforetext.innerText = `${operationValue} ${operation}`;
             this.aftertext.innerText = "";
        }
    }



     changeOperation(operation) {
        const mathOperations = ["x", "÷", "+", "-"]

        if(!mathOperations.includes(operation)) {
            return;
        }

        this.beforetext.innerText = this.beforetext.innerText.slice(0, -1) + operation;
     }

     processDelOperator() {
        this.aftertext.innerText = this.aftertext.innerText.slice(0, -1);
     }

     clearCurrentOperation(){
        this.aftertext.innerText = "";
     }

     clearAllOperation() {
        this.aftertext.innerText = "";
        this.beforetext.innerText = "";
     }

     EqualOperation() {
        const operation = beforetext.innerText.split(" ")[1];

        this.processOperation(operation);

        const result = document.getElementById("#before").value
        aftertext.textContent = result;
     }
}

const calc = new calculator(beforetext, aftertext, buttons);

buttons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        const value = e.target.innerText;

        if(+value >= 0 || value === ".") {
            calc.addDigit(value)
        } else {
            calc.processOperation(value)
        }
    });
}); 
