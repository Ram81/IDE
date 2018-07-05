import React from 'react';

class AddCommentTooltip extends React.Component {
  constructor(props) {
    super(props);
    this.onEnterPress = this.onEnterPress.bind(this);
    this.onCommentChange = this.onCommentChange.bind(this);
  }

  onEnterPress(event) {
    if(event.keyCode == 13 && event.shiftKey == false) {
      event.preventDefault();
      this.props.layer['comments'].push(this.refs.comment);
    }
  }

  onCommentChange(event) {
    this.setState({comment: event.target.value});
  }
  
  render() {
      return (
        <div style={{ textAlign: 'left', color: "#000"}}>
          <div className="row" style={{ paddingLeft: '15px'}}>
            <div className="col-md-2" style={{padding: '0px', paddingLeft: '6px'}}>
              <img src={'/static/img/user.png'} className="img-responsive" alt="user" height="40px" width="40px"/>
            </div>
            <div className="col-md-10" style={{ padding: '0px'}}>
              <textarea className="CommentTextarea" placeholder="Add your comment here...">
              </textarea>
            </div>
          </div>
          <div className="row" style={{ paddingLeft: '20px', paddingTop: '10px'}}>
            <div className="col-md-4 col-md-offset-8" style={{padding: '0px', textAlign: 'left', paddingLeft: '6px' }}>
              <button className="btn btn-success text-center" id='btn-comment' disabled={this.disableZoom}>
                  <span className="glyphicon glyphicon-comment" aria-hidden="true"></span> Comment
              </button>
            </div>
          </div>
        </div>
      )
  }
}

AddCommentTooltip.propTypes = {
  layer: React.PropTypes.object
};

export default AddCommentTooltip;
