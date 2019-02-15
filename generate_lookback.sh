melody_rnn_generate \
  --config=lookback_rnn \
  --bundle_file=./lookback_rnn.mag \
  --output_dir=./generated \
  --num_outputs=5 \
  --num_steps=128 \
  --primer_melody="[60]"