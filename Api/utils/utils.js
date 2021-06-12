exports.HttpError = class HttpError {
  constructor(statusCode, errMessage) {
    this.statusCode = statusCode;
    this.errMessage = errMessage;
  }
};
