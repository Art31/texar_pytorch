"""Configurations of Transformer model
"""
import copy

import texar.torch as tx

random_seed = 1234

beam_width = 3

length_penalty = 0.6
hidden_dim = 256

emb = {
    "name": "lookup_table",
    "dim": hidden_dim,
    "initializer": {
        "type": "normal_",
        "kwargs": {"mean": 0.0, "std": hidden_dim ** -0.5},
    },
}

position_embedder_hparams = {"dim": hidden_dim}

encoder = {
    "dim": hidden_dim,
    "num_blocks": 6,
    "multihead_attention": {
        "num_heads": 8,
        "output_dim": hidden_dim
        # See documentation for more optional hyperparameters
    },
    "initializer": {
        "type": "variance_scaling_initializer",
        "kwargs": {"factor": 1.0, "mode": "FAN_AVG", "uniform": True},
    },
    "poswise_feedforward": tx.modules.default_transformer_poswise_net_hparams(
        input_dim=hidden_dim,
        output_dim=hidden_dim
    ),
}

decoder = copy.deepcopy(encoder)

loss_label_confidence = 0.9

opt = {
    "optimizer": {
        "type": "Adam",
        "kwargs": {"beta1": 0.9, "beta2": 0.98, "epsilon": 1e-9},
    }
}

lr_config = {
    "learning_rate_schedule": "static", # "constant.linear_warmup.rsqrt_decay.rsqrt_depth",
    "lr_constant": 2 * (hidden_dim ** -0.5),
    "static_lr": 1e-4,
    "warmup_steps": 25000,
}
