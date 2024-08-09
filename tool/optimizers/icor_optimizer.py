def optimize_sequence(input_seq, sequence_type):
    # Load ONNX model
    model_path = os.path.join(os.getcwd(), 'tool', 'models', 'icor.onnx')
    sess = rt.InferenceSession(model_path)
    input_name = sess.get_inputs()[0].name

    # Define categorical labels and aa2int function
    labels = ['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACG', 'ACT', 'AGC', 'ATA', 'ATC', 'ATG', 'ATT', 'CAA', 'CAC', 'CAG', 'CCG', 'CCT', 'CTA', 'CTC', 'CTG', 'CTT', 'GAA', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT', 'GGA', 'GGC', 'GTC', 'GTG', 'GTT', 'TAA', 'TAT', 'TCA', 'TCG', 'TCT', 'TGG', 'TGT', 'TTA', 'TTC', 'TTG', 'TTT', 'ACC', 'CAT', 'CCA', 'CGG', 'CGT', 'GAC', 'GAG', 'GGT', 'AGT', 'GGG', 'GTA', 'TGC', 'CCC', 'CGA', 'CGC', 'TAC', 'TAG', 'TCC', 'AGA', 'AGG', 'TGA']

    def aa2int(seq):
        _aa2int = {'A': 1, 'R': 2, 'N': 3, 'D': 4, 'C': 5, 'Q': 6, 'E': 7, 'G': 8, 'H': 9, 'I': 10, 'L': 11, 'K': 12, 'M': 13, 'F': 14, 'P': 15, 'S': 16, 'T': 17, 'W': 18, 'Y': 19, 'V': 20, 'B': 21, 'Z': 22, 'X': 23, '*': 24, '-': 25, '?': 26}
        return [_aa2int[i] for i in seq]

    # Process input sequence
    if sequence_type == 'DNA':
        input_seq = str(Seq(input_seq).translate())

    # One-hot encode the amino acid sequence
    oh_array = np.zeros(shape=(26, len(input_seq)))
    aa_placement = aa2int(input_seq)
    for i in range(len(aa_placement)):
        oh_array[aa_placement[i], i] = 1

    # Prepare input for ONNX model
    x = np.array(np.transpose([oh_array]))
    y = x.astype(np.float32)
    y = np.reshape(y, (y.shape[0], 1, 26))

    # Get prediction
    pred_onx = sess.run(None, {input_name: y})

    # Get the index of the highest probability from softmax output
    pred_indices = [np.argmax(pred) for pred in pred_onx[0]]

    # Convert indices to optimized sequence
    out_str = ''.join([labels[index] for index in pred_indices])

    return out_str

# Test the function
test_seq = "ATGAGCGACGTGGCTATTGTGAAGGAG"
test_result = optimize_sequence(test_seq, "DNA")
print(f"Test result: {test_result}")
