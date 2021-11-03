max_batch_tokens = 2048
test_batch_size = 32

max_train_epoch = 40
display_steps = 500
eval_steps = 2500

max_decoding_length = 256

filename_prefix = "processed."
input_dir = 'temp/run_pt_en_bpe/data'
vocab_file = input_dir + '/processed.vocab.text'
encoding = "bpe"
