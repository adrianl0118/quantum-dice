from qiskit import QuantumCircuit, execute, Aer, IBMQ, ClassicalRegister, QuantumRegister
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.quantum_info import Pauli, state_fidelity, basis_state, process_fidelity
from qiskit.tools.monitor import job_monitor

if __name__ == "__main__":

    # Load IBMQ account (first time usage required save_account with token) and choose quantum computer terminal
    IBMQ.load_account()
    provider = IBMQ.get_provider('ibm-q')
    qcomp = provider.get_backend('ibmq_12_yorktown')

    # Set up five quantum bits to be superpositioned and five classical bits for storing measurements
    circuit = QuantumCircuit(5,5)

    # Add Hadamard Gates to create entanglement
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.h(4)

    # Set up measurements - store measurements from quantum register in classical register
    circuit.measure([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])

    # Collapse bits 8192 times, generates a random number between 0 and 31 (five bits, max is 2^5 = 32) over eight thousand times
    shots = 8192   # This is the maximum amount of shots you are allowed to take from an IBM Quantum Computer in one sitting
    job = execute(circuit,qcomp,shots=shots,memory=True)
    job_monitor(job)

    result = job.result()
    memory = result.get_memory()

    # Print in comma delimited form for copy/paste into javascript vector and into Excel file for analysis
    diceResults = []
    print("Quantum numbers generated by quantum computers at IBM are: ")
    for x in range(0, shots):
       diceResults.append(int(memory[x],2))

    print(diceResults)