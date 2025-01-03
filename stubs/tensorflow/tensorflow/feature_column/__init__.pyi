"""Public API for tf._api.v2.feature_column namespace"""

from collections.abc import Callable, Iterable, Sequence

import tensorflow as tf
from tensorflow._aliases import ShapeLike
from tensorflow.python.feature_column import feature_column_v2 as fc, sequence_feature_column as seq_fc

def numeric_column(
    key: str,
    shape: ShapeLike = (1,),
    default_value: float | None = None,
    dtype: tf.DType = ...,
    normalizer_fn: Callable[[tf.Tensor], tf.Tensor] | None = None,
) -> fc.NumericColumn:
    """
    Represents real valued or numerical features. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Example:

    Assume we have data with two features `a` and `b`.

    >>> data = {'a': [15, 9, 17, 19, 21, 18, 25, 30],
    ...    'b': [5.0, 6.4, 10.5, 13.6, 15.7, 19.9, 20.3 , 0.0]}

    Let us represent the features `a` and `b` as numerical features.

    >>> a = tf.feature_column.numeric_column('a')
    >>> b = tf.feature_column.numeric_column('b')

    Feature column describe a set of transformations to the inputs.

    For example, to "bucketize" feature `a`, wrap the `a` column in a
    `feature_column.bucketized_column`.
    Providing `5` bucket boundaries, the bucketized_column api
    will bucket this feature in total of `6` buckets.

    >>> a_buckets = tf.feature_column.bucketized_column(a,
    ...    boundaries=[10, 15, 20, 25, 30])

    Create a `DenseFeatures` layer which will apply the transformations
    described by the set of `tf.feature_column` objects:

    >>> feature_layer = tf.keras.layers.DenseFeatures([a_buckets, b])
    >>> print(feature_layer(data))
    tf.Tensor(
    [[ 0.   0.   1.   0.   0.   0.   5. ]
     [ 1.   0.   0.   0.   0.   0.   6.4]
     [ 0.   0.   1.   0.   0.   0.  10.5]
     [ 0.   0.   1.   0.   0.   0.  13.6]
     [ 0.   0.   0.   1.   0.   0.  15.7]
     [ 0.   0.   1.   0.   0.   0.  19.9]
     [ 0.   0.   0.   0.   1.   0.  20.3]
     [ 0.   0.   0.   0.   0.   1.   0. ]], shape=(8, 7), dtype=float32)

    Args:
      key: A unique string identifying the input feature. It is used as the column
        name and the dictionary key for feature parsing configs, feature `Tensor`
        objects, and feature columns.
      shape: An iterable of integers specifies the shape of the `Tensor`. An
        integer can be given which means a single dimension `Tensor` with given
        width. The `Tensor` representing the column will have the shape of
        [batch_size] + `shape`.
      default_value: A single value compatible with `dtype` or an iterable of
        values compatible with `dtype` which the column takes on during
        `tf.Example` parsing if data is missing. A default value of `None` will
        cause `tf.io.parse_example` to fail if an example does not contain this
        column. If a single value is provided, the same value will be applied as
        the default value for every item. If an iterable of values is provided,
        the shape of the `default_value` should be equal to the given `shape`.
      dtype: defines the type of values. Default value is `tf.float32`. Must be a
        non-quantized, real integer or floating point type.
      normalizer_fn: If not `None`, a function that can be used to normalize the
        value of the tensor after `default_value` is applied for parsing.
        Normalizer function takes the input `Tensor` as its argument, and returns
        the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that
        even though the most common use case of this function is normalization, it
        can be used for any kind of Tensorflow transformations.

    Returns:
      A `NumericColumn`.

    Raises:
      TypeError: if any dimension in shape is not an int
      ValueError: if any dimension in shape is not a positive integer
      TypeError: if `default_value` is an iterable but not compatible with `shape`
      TypeError: if `default_value` is not compatible with `dtype`.
      ValueError: if `dtype` is not convertible to `tf.float32`.
    """
    ...
def bucketized_column(source_column: fc.NumericColumn, boundaries: list[float] | tuple[float, ...]) -> fc.BucketizedColumn:
    """
    Represents discretized dense input bucketed by `boundaries`. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Buckets include the left boundary, and exclude the right boundary. Namely,
    `boundaries=[0., 1., 2.]` generates buckets `(-inf, 0.)`, `[0., 1.)`,
    `[1., 2.)`, and `[2., +inf)`.

    For example, if the inputs are

    ```python
    boundaries = [0, 10, 100]
    input tensor = [[-5, 10000]
                    [150,   10]
                    [5,    100]]
    ```

    then the output will be

    ```python
    output = [[0, 3]
              [3, 2]
              [1, 3]]
    ```

    Example:

    ```python
    price = tf.feature_column.numeric_column('price')
    bucketized_price = tf.feature_column.bucketized_column(
        price, boundaries=[...])
    columns = [bucketized_price, ...]
    features = tf.io.parse_example(
        ..., features=tf.feature_column.make_parse_example_spec(columns))
    dense_tensor = tf.keras.layers.DenseFeatures(columns)(features)
    ```

    A `bucketized_column` can also be crossed with another categorical column
    using `crossed_column`:

    ```python
    price = tf.feature_column.numeric_column('price')
    # bucketized_column converts numerical feature to a categorical one.
    bucketized_price = tf.feature_column.bucketized_column(
        price, boundaries=[...])
    # 'keywords' is a string feature.
    price_x_keywords = tf.feature_column.crossed_column(
        [bucketized_price, 'keywords'], 50K)
    columns = [price_x_keywords, ...]
    features = tf.io.parse_example(
        ..., features=tf.feature_column.make_parse_example_spec(columns))
    dense_tensor = tf.keras.layers.DenseFeatures(columns)(features)
    linear_model = tf.keras.experimental.LinearModel(units=...)(dense_tensor)
    ```

    Args:
      source_column: A one-dimensional dense column which is generated with
        `numeric_column`.
      boundaries: A sorted list or tuple of floats specifying the boundaries.

    Returns:
      A `BucketizedColumn`.

    Raises:
      ValueError: If `source_column` is not a numeric column, or if it is not
        one-dimensional.
      ValueError: If `boundaries` is not a sorted list or tuple.
    """
    ...
def embedding_column(
    categorical_column: fc.CategoricalColumn,
    dimension: int,
    combiner: fc._Combiners = "mean",
    initializer: Callable[[ShapeLike], tf.Tensor] | None = None,
    ckpt_to_load_from: str | None = None,
    tensor_name_in_ckpt: str | None = None,
    max_norm: float | None = None,
    trainable: bool = True,
    use_safe_embedding_lookup: bool = True,
) -> fc.EmbeddingColumn:
    """
    `DenseColumn` that converts from sparse, categorical input. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Use this when your inputs are sparse, but you want to convert them to a dense
    representation (e.g., to feed to a DNN).

    Args:
      categorical_column: A `CategoricalColumn` created by a
        `categorical_column_with_*` function. This column produces the sparse IDs
        that are inputs to the embedding lookup.
      dimension: An integer specifying dimension of the embedding, must be > 0.
      combiner: A string specifying how to reduce if there are multiple entries in
        a single row. Currently 'mean', 'sqrtn' and 'sum' are supported, with
        'mean' the default. 'sqrtn' often achieves good accuracy, in particular
        with bag-of-words columns. Each of this can be thought as example level
        normalizations on the column. For more information, see
        `tf.embedding_lookup_sparse`.
      initializer: A variable initializer function to be used in embedding
        variable initialization. If not specified, defaults to
        `truncated_normal_initializer` with mean `0.0` and standard deviation
        `1/sqrt(dimension)`.
      ckpt_to_load_from: String representing checkpoint name/pattern from which to
        restore column weights. Required if `tensor_name_in_ckpt` is not `None`.
      tensor_name_in_ckpt: Name of the `Tensor` in `ckpt_to_load_from` from which
        to restore the column weights. Required if `ckpt_to_load_from` is not
        `None`.
      max_norm: If not `None`, embedding values are l2-normalized to this value.
      trainable: Whether or not the embedding is trainable. Default is True.
      use_safe_embedding_lookup: If true, uses safe_embedding_lookup_sparse
        instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
        there are no empty rows and all weights and ids are positive at the
        expense of extra compute cost. This only applies to rank 2 (NxM) shaped
        input tensors. Defaults to true, consider turning off if the above checks
        are not needed. Note that having empty rows will not trigger any error
        though the output result might be 0 or omitted.

    Returns:
      `DenseColumn` that converts from sparse input.

    Raises:
      ValueError: if `dimension` not > 0.
      ValueError: if exactly one of `ckpt_to_load_from` and `tensor_name_in_ckpt`
        is specified.
      ValueError: if `initializer` is specified and is not callable.
      RuntimeError: If eager execution is enabled.
    """
    ...
def shared_embeddings(
    categorical_columns: Iterable[fc.CategoricalColumn],
    dimension: int,
    combiner: fc._Combiners = "mean",
    initializer: Callable[[ShapeLike], tf.Tensor] | None = None,
    shared_embedding_collection_name: str | None = None,
    ckpt_to_load_from: str | None = None,
    tensor_name_in_ckpt: str | None = None,
    max_norm: float | None = None,
    trainable: bool = True,
    use_safe_embedding_lookup: bool = True,
) -> list[fc.SharedEmbeddingColumn]:
    """
    List of dense columns that convert from sparse, categorical input. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    This is similar to `embedding_column`, except that it produces a list of
    embedding columns that share the same embedding weights.

    Use this when your inputs are sparse and of the same type (e.g. watched and
    impression video IDs that share the same vocabulary), and you want to convert
    them to a dense representation (e.g., to feed to a DNN).

    Inputs must be a list of categorical columns created by any of the
    `categorical_column_*` function. They must all be of the same type and have
    the same arguments except `key`. E.g. they can be
    categorical_column_with_vocabulary_file with the same vocabulary_file. Some or
    all columns could also be weighted_categorical_column.

    Args:
      categorical_columns: List of categorical columns created by a
        `categorical_column_with_*` function. These columns produce the sparse IDs
        that are inputs to the embedding lookup. All columns must be of the same
        type and have the same arguments except `key`. E.g. they can be
        categorical_column_with_vocabulary_file with the same vocabulary_file.
        Some or all columns could also be weighted_categorical_column.
      dimension: An integer specifying dimension of the embedding, must be > 0.
      combiner: A string specifying how to reduce if there are multiple entries in
        a single row. Currently 'mean', 'sqrtn' and 'sum' are supported, with
        'mean' the default. 'sqrtn' often achieves good accuracy, in particular
        with bag-of-words columns. Each of this can be thought as example level
        normalizations on the column. For more information, see
        `tf.embedding_lookup_sparse`.
      initializer: A variable initializer function to be used in embedding
        variable initialization. If not specified, defaults to
        `truncated_normal_initializer` with mean `0.0` and standard deviation
        `1/sqrt(dimension)`.
      shared_embedding_collection_name: Optional collective name of these columns.
        If not given, a reasonable name will be chosen based on the names of
        `categorical_columns`.
      ckpt_to_load_from: String representing checkpoint name/pattern from which to
        restore column weights. Required if `tensor_name_in_ckpt` is not `None`.
      tensor_name_in_ckpt: Name of the `Tensor` in `ckpt_to_load_from` from which
        to restore the column weights. Required if `ckpt_to_load_from` is not
        `None`.
      max_norm: If not `None`, each embedding is clipped if its l2-norm is larger
        than this value, before combining.
      trainable: Whether or not the embedding is trainable. Default is True.
      use_safe_embedding_lookup: If true, uses safe_embedding_lookup_sparse
        instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
        there are no empty rows and all weights and ids are positive at the
        expense of extra compute cost. This only applies to rank 2 (NxM) shaped
        input tensors. Defaults to true, consider turning off if the above checks
        are not needed. Note that having empty rows will not trigger any error
        though the output result might be 0 or omitted.

    Returns:
      A list of dense columns that converts from sparse input. The order of
      results follows the ordering of `categorical_columns`.

    Raises:
      ValueError: if `dimension` not > 0.
      ValueError: if any of the given `categorical_columns` is of different type
        or has different arguments than the others.
      ValueError: if exactly one of `ckpt_to_load_from` and `tensor_name_in_ckpt`
        is specified.
      ValueError: if `initializer` is specified and is not callable.
      RuntimeError: if eager execution is enabled.
    """
    ...
def categorical_column_with_identity(
    key: str, num_buckets: int, default_value: int | None = None
) -> fc.IdentityCategoricalColumn:
    """
    A `CategoricalColumn` that returns identity values. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Use this when your inputs are integers in the range `[0, num_buckets)`, and
    you want to use the input value itself as the categorical ID. Values outside
    this range will result in `default_value` if specified, otherwise it will
    fail.

    Typically, this is used for contiguous ranges of integer indexes, but
    it doesn't have to be. This might be inefficient, however, if many of IDs
    are unused. Consider `categorical_column_with_hash_bucket` in that case.

    For input dictionary `features`, `features[key]` is either `Tensor` or
    `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
    and `''` for string, which will be dropped by this feature column.

    In the following examples, each input in the range `[0, 1000000)` is assigned
    the same value. All other inputs are assigned `default_value` 0. Note that a
    literal 0 in inputs will result in the same default ID.

    Linear model:

    ```python
    import tensorflow as tf
    video_id = tf.feature_column.categorical_column_with_identity(
        key='video_id', num_buckets=1000000, default_value=0)
    columns = [video_id]
    features = {'video_id': tf.sparse.from_dense([[2, 85, 0, 0, 0],
    [33,78, 2, 73, 1]])}
    linear_prediction = tf.compat.v1.feature_column.linear_model(features,
    columns)
    ```

    Embedding for a DNN model:

    ```python
    import tensorflow as tf
    video_id = tf.feature_column.categorical_column_with_identity(
        key='video_id', num_buckets=1000000, default_value=0)
    columns = [tf.feature_column.embedding_column(video_id, 9)]
    features = {'video_id': tf.sparse.from_dense([[2, 85, 0, 0, 0],
    [33,78, 2, 73, 1]])}
    input_layer = tf.keras.layers.DenseFeatures(columns)
    dense_tensor = input_layer(features)
    ```

    Args:
      key: A unique string identifying the input feature. It is used as the column
        name and the dictionary key for feature parsing configs, feature `Tensor`
        objects, and feature columns.
      num_buckets: Range of inputs and outputs is `[0, num_buckets)`.
      default_value: If set, values outside of range `[0, num_buckets)` will be
        replaced with this value. If not set, values >= num_buckets will cause a
        failure while values < 0 will be dropped.

    Returns:
      A `CategoricalColumn` that returns identity values.

    Raises:
      ValueError: if `num_buckets` is less than one.
      ValueError: if `default_value` is not in range `[0, num_buckets)`.
    """
    ...
def categorical_column_with_hash_bucket(key: str, hash_bucket_size: int, dtype: tf.DType = ...) -> fc.HashedCategoricalColumn:
    """
    Represents sparse feature where ids are set by hashing. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Use this when your sparse features are in string or integer format, and you
    want to distribute your inputs into a finite number of buckets by hashing.
    output_id = Hash(input_feature_string) % bucket_size for string type input.
    For int type input, the value is converted to its string representation first
    and then hashed by the same formula.

    For input dictionary `features`, `features[key]` is either `Tensor` or
    `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
    and `''` for string, which will be dropped by this feature column.

    Example:

    ```python
    import tensorflow as tf
    keywords = tf.feature_column.categorical_column_with_hash_bucket("keywords",
    10000)
    columns = [keywords]
    features = {'keywords': tf.constant([['Tensorflow', 'Keras', 'RNN', 'LSTM',
    'CNN'], ['LSTM', 'CNN', 'Tensorflow', 'Keras', 'RNN'], ['CNN', 'Tensorflow',
    'LSTM', 'Keras', 'RNN']])}
    linear_prediction, _, _ = tf.compat.v1.feature_column.linear_model(features,
    columns)

    # or
    import tensorflow as tf
    keywords = tf.feature_column.categorical_column_with_hash_bucket("keywords",
    10000)
    keywords_embedded = tf.feature_column.embedding_column(keywords, 16)
    columns = [keywords_embedded]
    features = {'keywords': tf.constant([['Tensorflow', 'Keras', 'RNN', 'LSTM',
    'CNN'], ['LSTM', 'CNN', 'Tensorflow', 'Keras', 'RNN'], ['CNN', 'Tensorflow',
    'LSTM', 'Keras', 'RNN']])}
    input_layer = tf.keras.layers.DenseFeatures(columns)
    dense_tensor = input_layer(features)
    ```

    Args:
      key: A unique string identifying the input feature. It is used as the column
        name and the dictionary key for feature parsing configs, feature `Tensor`
        objects, and feature columns.
      hash_bucket_size: An int > 1. The number of buckets.
      dtype: The type of features. Only string and integer types are supported.

    Returns:
      A `HashedCategoricalColumn`.

    Raises:
      ValueError: `hash_bucket_size` is not greater than 1.
      ValueError: `dtype` is neither string nor integer.
    """
    ...
def categorical_column_with_vocabulary_file(
    key: str,
    vocabulary_file: str,
    vocabulary_size: int | None = None,
    dtype: tf.DType = ...,
    default_value: str | int | None = None,
    num_oov_buckets: int = 0,
    file_format: str | None = None,
) -> fc.VocabularyFileCategoricalColumn:
    """
    A `CategoricalColumn` with a vocabulary file. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Use this when your inputs are in string or integer format, and you have a
    vocabulary file that maps each value to an integer ID. By default,
    out-of-vocabulary values are ignored. Use either (but not both) of
    `num_oov_buckets` and `default_value` to specify how to include
    out-of-vocabulary values.

    For input dictionary `features`, `features[key]` is either `Tensor` or
    `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
    and `''` for string, which will be dropped by this feature column.

    Example with `num_oov_buckets`:
    File `'/us/states.txt'` contains 50 lines, each with a 2-character U.S. state
    abbreviation. All inputs with values in that file are assigned an ID 0-49,
    corresponding to its line number. All other values are hashed and assigned an
    ID 50-54.

    ```python
    states = categorical_column_with_vocabulary_file(
        key='states', vocabulary_file='/us/states.txt', vocabulary_size=50,
        num_oov_buckets=5)
    columns = [states, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction = linear_model(features, columns)
    ```

    Example with `default_value`:
    File `'/us/states.txt'` contains 51 lines - the first line is `'XX'`, and the
    other 50 each have a 2-character U.S. state abbreviation. Both a literal
    `'XX'` in input, and other values missing from the file, will be assigned
    ID 0. All others are assigned the corresponding line number 1-50.

    ```python
    states = categorical_column_with_vocabulary_file(
        key='states', vocabulary_file='/us/states.txt', vocabulary_size=51,
        default_value=0)
    columns = [states, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction, _, _ = linear_model(features, columns)
    ```

    And to make an embedding with either:

    ```python
    columns = [embedding_column(states, 3),...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    dense_tensor = input_layer(features, columns)
    ```

    Args:
      key: A unique string identifying the input feature. It is used as the column
        name and the dictionary key for feature parsing configs, feature `Tensor`
        objects, and feature columns.
      vocabulary_file: The vocabulary file name.
      vocabulary_size: Number of the elements in the vocabulary. This must be no
        greater than length of `vocabulary_file`, if less than length, later
        values are ignored. If None, it is set to the length of `vocabulary_file`.
      dtype: The type of features. Only string and integer types are supported.
      default_value: The integer ID value to return for out-of-vocabulary feature
        values, defaults to `-1`. This can not be specified with a positive
        `num_oov_buckets`.
      num_oov_buckets: Non-negative integer, the number of out-of-vocabulary
        buckets. All out-of-vocabulary inputs will be assigned IDs in the range
        `[vocabulary_size, vocabulary_size+num_oov_buckets)` based on a hash of
        the input value. A positive `num_oov_buckets` can not be specified with
        `default_value`.
      file_format: The format of the vocabulary file. The format is 'text' by
        default unless `vocabulary_file` is a string which ends in 'tfrecord.gz'.
        Accepted alternative value for `file_format` is 'tfrecord_gzip'.

    Returns:
      A `CategoricalColumn` with a vocabulary file.

    Raises:
      ValueError: `vocabulary_file` is missing or cannot be opened.
      ValueError: `vocabulary_size` is missing or < 1.
      ValueError: `num_oov_buckets` is a negative integer.
      ValueError: `num_oov_buckets` and `default_value` are both specified.
      ValueError: `dtype` is neither string nor integer.
    """
    ...
def categorical_column_with_vocabulary_list(
    key: str,
    vocabulary_list: Sequence[str] | Sequence[int],
    dtype: tf.DType | None = None,
    default_value: str | int | None = -1,
    num_oov_buckets: int = 0,
) -> fc.VocabularyListCategoricalColumn:
    """
    A `CategoricalColumn` with in-memory vocabulary. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Use this when your inputs are in string or integer format, and you have an
    in-memory vocabulary mapping each value to an integer ID. By default,
    out-of-vocabulary values are ignored. Use either (but not both) of
    `num_oov_buckets` and `default_value` to specify how to include
    out-of-vocabulary values.

    For input dictionary `features`, `features[key]` is either `Tensor` or
    `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
    and `''` for string, which will be dropped by this feature column.

    Example with `num_oov_buckets`:
    In the following example, each input in `vocabulary_list` is assigned an ID
    0-3 corresponding to its index (e.g., input 'B' produces output 2). All other
    inputs are hashed and assigned an ID 4-5.

    ```python
    colors = categorical_column_with_vocabulary_list(
        key='colors', vocabulary_list=('R', 'G', 'B', 'Y'),
        num_oov_buckets=2)
    columns = [colors, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction, _, _ = linear_model(features, columns)
    ```

    Example with `default_value`:
    In the following example, each input in `vocabulary_list` is assigned an ID
    0-4 corresponding to its index (e.g., input 'B' produces output 3). All other
    inputs are assigned `default_value` 0.


    ```python
    colors = categorical_column_with_vocabulary_list(
        key='colors', vocabulary_list=('X', 'R', 'G', 'B', 'Y'), default_value=0)
    columns = [colors, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction, _, _ = linear_model(features, columns)
    ```

    And to make an embedding with either:

    ```python
    columns = [embedding_column(colors, 3),...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    dense_tensor = input_layer(features, columns)
    ```

    Args:
      key: A unique string identifying the input feature. It is used as the column
        name and the dictionary key for feature parsing configs, feature `Tensor`
        objects, and feature columns.
      vocabulary_list: An ordered iterable defining the vocabulary. Each feature
        is mapped to the index of its value (if present) in `vocabulary_list`.
        Must be castable to `dtype`.
      dtype: The type of features. Only string and integer types are supported. If
        `None`, it will be inferred from `vocabulary_list`.
      default_value: The integer ID value to return for out-of-vocabulary feature
        values, defaults to `-1`. This can not be specified with a positive
        `num_oov_buckets`.
      num_oov_buckets: Non-negative integer, the number of out-of-vocabulary
        buckets. All out-of-vocabulary inputs will be assigned IDs in the range
        `[len(vocabulary_list), len(vocabulary_list)+num_oov_buckets)` based on a
        hash of the input value. A positive `num_oov_buckets` can not be specified
        with `default_value`.

    Returns:
      A `CategoricalColumn` with in-memory vocabulary.

    Raises:
      ValueError: if `vocabulary_list` is empty, or contains duplicate keys.
      ValueError: `num_oov_buckets` is a negative integer.
      ValueError: `num_oov_buckets` and `default_value` are both specified.
      ValueError: if `dtype` is not integer or string.
    """
    ...
def indicator_column(categorical_column: fc.CategoricalColumn) -> fc.IndicatorColumn:
    """
    Represents multi-hot representation of given categorical column. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    - For DNN model, `indicator_column` can be used to wrap any
      `categorical_column_*` (e.g., to feed to DNN). Consider to Use
      `embedding_column` if the number of buckets/unique(values) are large.

    - For Wide (aka linear) model, `indicator_column` is the internal
      representation for categorical column when passing categorical column
      directly (as any element in feature_columns) to `linear_model`. See
      `linear_model` for details.

    ```python
    name = indicator_column(categorical_column_with_vocabulary_list(
        'name', ['bob', 'george', 'wanda']))
    columns = [name, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    dense_tensor = input_layer(features, columns)

    dense_tensor == [[1, 0, 0]]  # If "name" bytes_list is ["bob"]
    dense_tensor == [[1, 0, 1]]  # If "name" bytes_list is ["bob", "wanda"]
    dense_tensor == [[2, 0, 0]]  # If "name" bytes_list is ["bob", "bob"]
    ```

    Args:
      categorical_column: A `CategoricalColumn` which is created by
        `categorical_column_with_*` or `crossed_column` functions.

    Returns:
      An `IndicatorColumn`.

    Raises:
      ValueError: If `categorical_column` is not CategoricalColumn type.
    """
    ...
def weighted_categorical_column(
    categorical_column: fc.CategoricalColumn, weight_feature_key: str, dtype: tf.DType = ...
) -> fc.WeightedCategoricalColumn:
    """
    Applies weight values to a `CategoricalColumn`. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Use this when each of your sparse inputs has both an ID and a value. For
    example, if you're representing text documents as a collection of word
    frequencies, you can provide 2 parallel sparse input features ('terms' and
    'frequencies' below).

    Example:

    Input `tf.Example` objects:

    ```proto
    [
      features {
        feature {
          key: "terms"
          value {bytes_list {value: "very" value: "model"}}
        }
        feature {
          key: "frequencies"
          value {float_list {value: 0.3 value: 0.1}}
        }
      },
      features {
        feature {
          key: "terms"
          value {bytes_list {value: "when" value: "course" value: "human"}}
        }
        feature {
          key: "frequencies"
          value {float_list {value: 0.4 value: 0.1 value: 0.2}}
        }
      }
    ]
    ```

    ```python
    categorical_column = categorical_column_with_hash_bucket(
        column_name='terms', hash_bucket_size=1000)
    weighted_column = weighted_categorical_column(
        categorical_column=categorical_column, weight_feature_key='frequencies')
    columns = [weighted_column, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction, _, _ = linear_model(features, columns)
    ```

    This assumes the input dictionary contains a `SparseTensor` for key
    'terms', and a `SparseTensor` for key 'frequencies'. These 2 tensors must have
    the same indices and dense shape.

    Args:
      categorical_column: A `CategoricalColumn` created by
        `categorical_column_with_*` functions.
      weight_feature_key: String key for weight values.
      dtype: Type of weights, such as `tf.float32`. Only float and integer weights
        are supported.

    Returns:
      A `CategoricalColumn` composed of two sparse features: one represents id,
      the other represents weight (value) of the id feature in that example.

    Raises:
      ValueError: if `dtype` is not convertible to float.
    """
    ...
def crossed_column(
    keys: Iterable[str | fc.CategoricalColumn], hash_bucket_size: int, hash_key: int | None = None
) -> fc.CrossedColumn:
    """
    Returns a column for performing crosses of categorical features. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use `tf.keras.layers.experimental.preprocessing.HashedCrossing` instead for feature crossing when preprocessing data to train a Keras model.

    Crossed features will be hashed according to `hash_bucket_size`. Conceptually,
    the transformation can be thought of as:
      Hash(cartesian product of features) % `hash_bucket_size`

    For example, if the input features are:

    * SparseTensor referred by first key:

      ```python
      shape = [2, 2]
      {
          [0, 0]: "a"
          [1, 0]: "b"
          [1, 1]: "c"
      }
      ```

    * SparseTensor referred by second key:

      ```python
      shape = [2, 1]
      {
          [0, 0]: "d"
          [1, 0]: "e"
      }
      ```

    then crossed feature will look like:

    ```python
     shape = [2, 2]
    {
        [0, 0]: Hash64("d", Hash64("a")) % hash_bucket_size
        [1, 0]: Hash64("e", Hash64("b")) % hash_bucket_size
        [1, 1]: Hash64("e", Hash64("c")) % hash_bucket_size
    }
    ```

    Here is an example to create a linear model with crosses of string features:

    ```python
    keywords_x_doc_terms = crossed_column(['keywords', 'doc_terms'], 50K)
    columns = [keywords_x_doc_terms, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction = linear_model(features, columns)
    ```

    You could also use vocabulary lookup before crossing:

    ```python
    keywords = categorical_column_with_vocabulary_file(
        'keywords', '/path/to/vocabulary/file', vocabulary_size=1K)
    keywords_x_doc_terms = crossed_column([keywords, 'doc_terms'], 50K)
    columns = [keywords_x_doc_terms, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction = linear_model(features, columns)
    ```

    If an input feature is of numeric type, you can use
    `categorical_column_with_identity`, or `bucketized_column`, as in the example:

    ```python
    # vertical_id is an integer categorical feature.
    vertical_id = categorical_column_with_identity('vertical_id', 10K)
    price = numeric_column('price')
    # bucketized_column converts numerical feature to a categorical one.
    bucketized_price = bucketized_column(price, boundaries=[...])
    vertical_id_x_price = crossed_column([vertical_id, bucketized_price], 50K)
    columns = [vertical_id_x_price, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction = linear_model(features, columns)
    ```

    To use crossed column in DNN model, you need to add it in an embedding column
    as in this example:

    ```python
    vertical_id_x_price = crossed_column([vertical_id, bucketized_price], 50K)
    vertical_id_x_price_embedded = embedding_column(vertical_id_x_price, 10)
    dense_tensor = input_layer(features, [vertical_id_x_price_embedded, ...])
    ```

    Args:
      keys: An iterable identifying the features to be crossed. Each element can
        be either:
        * string: Will use the corresponding feature which must be of string type.
        * `CategoricalColumn`: Will use the transformed tensor produced by this
          column. Does not support hashed categorical column.
      hash_bucket_size: An int > 1. The number of buckets.
      hash_key: Specify the hash_key that will be used by the `FingerprintCat64`
        function to combine the crosses fingerprints on SparseCrossOp (optional).

    Returns:
      A `CrossedColumn`.

    Raises:
      ValueError: If `len(keys) < 2`.
      ValueError: If any of the keys is neither a string nor `CategoricalColumn`.
      ValueError: If any of the keys is `HashedCategoricalColumn`.
      ValueError: If `hash_bucket_size < 1`.
    """
    ...
def sequence_numeric_column(
    key: str,
    shape: ShapeLike = (1,),
    default_value: float = 0.0,
    dtype: tf.DType = ...,
    normalizer_fn: Callable[[tf.Tensor], tf.Tensor] | None = None,
) -> seq_fc.SequenceNumericColumn:
    """
    Returns a feature column that represents sequences of numeric data. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Example:

    ```python
    temperature = sequence_numeric_column('temperature')
    columns = [temperature]

    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    sequence_feature_layer = SequenceFeatures(columns)
    sequence_input, sequence_length = sequence_feature_layer(features)
    sequence_length_mask = tf.sequence_mask(sequence_length)

    rnn_cell = tf.keras.layers.SimpleRNNCell(hidden_size)
    rnn_layer = tf.keras.layers.RNN(rnn_cell)
    outputs, state = rnn_layer(sequence_input, mask=sequence_length_mask)
    ```

    Args:
      key: A unique string identifying the input features.
      shape: The shape of the input data per sequence id. E.g. if `shape=(2,)`,
        each example must contain `2 * sequence_length` values.
      default_value: A single value compatible with `dtype` that is used for
        padding the sparse data into a dense `Tensor`.
      dtype: The type of values.
      normalizer_fn: If not `None`, a function that can be used to normalize the
        value of the tensor after `default_value` is applied for parsing.
        Normalizer function takes the input `Tensor` as its argument, and returns
        the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that
        even though the most common use case of this function is normalization, it
        can be used for any kind of Tensorflow transformations.

    Returns:
      A `SequenceNumericColumn`.

    Raises:
      TypeError: if any dimension in shape is not an int.
      ValueError: if any dimension in shape is not a positive integer.
      ValueError: if `dtype` is not convertible to `tf.float32`.
    """
    ...
def sequence_categorical_column_with_identity(
    key: str, num_buckets: int, default_value: int | None = None
) -> fc.SequenceCategoricalColumn:
    """
    Returns a feature column that represents sequences of integers. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Pass this to `embedding_column` or `indicator_column` to convert sequence
    categorical data into dense representation for input to sequence NN, such as
    RNN.

    Example:

    ```python
    watches = sequence_categorical_column_with_identity(
        'watches', num_buckets=1000)
    watches_embedding = embedding_column(watches, dimension=10)
    columns = [watches_embedding]

    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    sequence_feature_layer = SequenceFeatures(columns)
    sequence_input, sequence_length = sequence_feature_layer(features)
    sequence_length_mask = tf.sequence_mask(sequence_length)

    rnn_cell = tf.keras.layers.SimpleRNNCell(hidden_size)
    rnn_layer = tf.keras.layers.RNN(rnn_cell)
    outputs, state = rnn_layer(sequence_input, mask=sequence_length_mask)
    ```

    Args:
      key: A unique string identifying the input feature.
      num_buckets: Range of inputs. Namely, inputs are expected to be in the range
        `[0, num_buckets)`.
      default_value: If `None`, this column's graph operations will fail for
        out-of-range inputs. Otherwise, this value must be in the range `[0,
        num_buckets)`, and will replace out-of-range inputs.

    Returns:
      A `SequenceCategoricalColumn`.

    Raises:
      ValueError: if `num_buckets` is less than one.
      ValueError: if `default_value` is not in range `[0, num_buckets)`.
    """
    ...
def sequence_categorical_column_with_hash_bucket(
    key: str, hash_bucket_size: int, dtype: tf.DType = ...
) -> fc.SequenceCategoricalColumn:
    """
    A sequence of categorical terms where ids are set by hashing. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Pass this to `embedding_column` or `indicator_column` to convert sequence
    categorical data into dense representation for input to sequence NN, such as
    RNN.

    Example:

    ```python
    tokens = sequence_categorical_column_with_hash_bucket(
        'tokens', hash_bucket_size=1000)
    tokens_embedding = embedding_column(tokens, dimension=10)
    columns = [tokens_embedding]

    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    sequence_feature_layer = SequenceFeatures(columns)
    sequence_input, sequence_length = sequence_feature_layer(features)
    sequence_length_mask = tf.sequence_mask(sequence_length)

    rnn_cell = tf.keras.layers.SimpleRNNCell(hidden_size)
    rnn_layer = tf.keras.layers.RNN(rnn_cell)
    outputs, state = rnn_layer(sequence_input, mask=sequence_length_mask)
    ```

    Args:
      key: A unique string identifying the input feature.
      hash_bucket_size: An int > 1. The number of buckets.
      dtype: The type of features. Only string and integer types are supported.

    Returns:
      A `SequenceCategoricalColumn`.

    Raises:
      ValueError: `hash_bucket_size` is not greater than 1.
      ValueError: `dtype` is neither string nor integer.
    """
    ...
def sequence_categorical_column_with_vocabulary_file(
    key: str,
    vocabulary_file: str,
    vocabulary_size: int | None = None,
    num_oov_buckets: int = 0,
    default_value: str | int | None = None,
    dtype: tf.DType = ...,
) -> fc.SequenceCategoricalColumn:
    """
    A sequence of categorical terms where ids use a vocabulary file. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Pass this to `embedding_column` or `indicator_column` to convert sequence
    categorical data into dense representation for input to sequence NN, such as
    RNN.

    Example:

    ```python
    states = sequence_categorical_column_with_vocabulary_file(
        key='states', vocabulary_file='/us/states.txt', vocabulary_size=50,
        num_oov_buckets=5)
    states_embedding = embedding_column(states, dimension=10)
    columns = [states_embedding]

    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    sequence_feature_layer = SequenceFeatures(columns)
    sequence_input, sequence_length = sequence_feature_layer(features)
    sequence_length_mask = tf.sequence_mask(sequence_length)

    rnn_cell = tf.keras.layers.SimpleRNNCell(hidden_size)
    rnn_layer = tf.keras.layers.RNN(rnn_cell)
    outputs, state = rnn_layer(sequence_input, mask=sequence_length_mask)
    ```

    Args:
      key: A unique string identifying the input feature.
      vocabulary_file: The vocabulary file name.
      vocabulary_size: Number of the elements in the vocabulary. This must be no
        greater than length of `vocabulary_file`, if less than length, later
        values are ignored. If None, it is set to the length of `vocabulary_file`.
      num_oov_buckets: Non-negative integer, the number of out-of-vocabulary
        buckets. All out-of-vocabulary inputs will be assigned IDs in the range
        `[vocabulary_size, vocabulary_size+num_oov_buckets)` based on a hash of
        the input value. A positive `num_oov_buckets` can not be specified with
        `default_value`.
      default_value: The integer ID value to return for out-of-vocabulary feature
        values, defaults to `-1`. This can not be specified with a positive
        `num_oov_buckets`.
      dtype: The type of features. Only string and integer types are supported.

    Returns:
      A `SequenceCategoricalColumn`.

    Raises:
      ValueError: `vocabulary_file` is missing or cannot be opened.
      ValueError: `vocabulary_size` is missing or < 1.
      ValueError: `num_oov_buckets` is a negative integer.
      ValueError: `num_oov_buckets` and `default_value` are both specified.
      ValueError: `dtype` is neither string nor integer.
    """
    ...
def sequence_categorical_column_with_vocabulary_list(
    key: str,
    vocabulary_list: Sequence[str] | Sequence[int],
    dtype: tf.DType | None = None,
    default_value: str | int | None = -1,
    num_oov_buckets: int = 0,
) -> fc.SequenceCategoricalColumn:
    """
    A sequence of categorical terms where ids use an in-memory list. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    Pass this to `embedding_column` or `indicator_column` to convert sequence
    categorical data into dense representation for input to sequence NN, such as
    RNN.

    Example:

    ```python
    colors = sequence_categorical_column_with_vocabulary_list(
        key='colors', vocabulary_list=('R', 'G', 'B', 'Y'),
        num_oov_buckets=2)
    colors_embedding = embedding_column(colors, dimension=3)
    columns = [colors_embedding]

    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    sequence_feature_layer = SequenceFeatures(columns)
    sequence_input, sequence_length = sequence_feature_layer(features)
    sequence_length_mask = tf.sequence_mask(sequence_length)

    rnn_cell = tf.keras.layers.SimpleRNNCell(hidden_size)
    rnn_layer = tf.keras.layers.RNN(rnn_cell)
    outputs, state = rnn_layer(sequence_input, mask=sequence_length_mask)
    ```

    Args:
      key: A unique string identifying the input feature.
      vocabulary_list: An ordered iterable defining the vocabulary. Each feature
        is mapped to the index of its value (if present) in `vocabulary_list`.
        Must be castable to `dtype`.
      dtype: The type of features. Only string and integer types are supported. If
        `None`, it will be inferred from `vocabulary_list`.
      default_value: The integer ID value to return for out-of-vocabulary feature
        values, defaults to `-1`. This can not be specified with a positive
        `num_oov_buckets`.
      num_oov_buckets: Non-negative integer, the number of out-of-vocabulary
        buckets. All out-of-vocabulary inputs will be assigned IDs in the range
        `[len(vocabulary_list), len(vocabulary_list)+num_oov_buckets)` based on a
        hash of the input value. A positive `num_oov_buckets` can not be specified
        with `default_value`.

    Returns:
      A `SequenceCategoricalColumn`.

    Raises:
      ValueError: if `vocabulary_list` is empty, or contains duplicate keys.
      ValueError: `num_oov_buckets` is a negative integer.
      ValueError: `num_oov_buckets` and `default_value` are both specified.
      ValueError: if `dtype` is not integer or string.
    """
    ...
def make_parse_example_spec(
    feature_columns: Iterable[fc._FeatureColumn],
) -> dict[str, tf.io.FixedLenFeature | tf.io.VarLenFeature]:
    """
    Creates parsing spec dictionary from input feature_columns. (deprecated)

    Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use Keras preprocessing layers instead, either directly or via the `tf.keras.utils.FeatureSpace` utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

    The returned dictionary can be used as arg 'features' in
    `tf.io.parse_example`.

    Typical usage example:

    ```python
    # Define features and transformations
    feature_a = tf.feature_column.categorical_column_with_vocabulary_file(...)
    feature_b = tf.feature_column.numeric_column(...)
    feature_c_bucketized = tf.feature_column.bucketized_column(
        tf.feature_column.numeric_column("feature_c"), ...)
    feature_a_x_feature_c = tf.feature_column.crossed_column(
        columns=["feature_a", feature_c_bucketized], ...)

    feature_columns = set(
        [feature_b, feature_c_bucketized, feature_a_x_feature_c])
    features = tf.io.parse_example(
        serialized=serialized_examples,
        features=tf.feature_column.make_parse_example_spec(feature_columns))
    ```

    For the above example, make_parse_example_spec would return the dict:

    ```python
    {
        "feature_a": parsing_ops.VarLenFeature(tf.string),
        "feature_b": parsing_ops.FixedLenFeature([1], dtype=tf.float32),
        "feature_c": parsing_ops.FixedLenFeature([1], dtype=tf.float32)
    }
    ```

    Args:
      feature_columns: An iterable containing all feature columns. All items
        should be instances of classes derived from `FeatureColumn`.

    Returns:
      A dict mapping each feature key to a `FixedLenFeature` or `VarLenFeature`
      value.

    Raises:
      ValueError: If any of the given `feature_columns` is not a `FeatureColumn`
        instance.
    """
    ...
